import asyncio
import getpass
import json
import os
import random

import websockets

from mapa import *
import sys
import math
import time
import random

#MAX_MOVES = 100


class SearchNode:
    def __init__(self, keeperPos, map, boxes = None):
        self.keeper = keeperPos
        self.map = map
        self.boxes = map.boxes if boxes == None else boxes[:]
        self.way = []
        self.positions = [keeperPos]
        self.cost = 0
        self.goals = self.map.filter_tiles([Tiles.BOX_ON_GOAL, Tiles.MAN_ON_GOAL, Tiles.GOAL])
        self.goals = [hash(elem) for elem in self.goals]


    def done(self):
        #goals = self.map.filter_tiles([Tiles.BOX_ON_GOAL, Tiles.MAN_ON_GOAL, Tiles.GOAL])
        for b in self.boxes:
            if hash(b) not in self.goals:
                return False
        return True
            
    def boxCanGo(self,boxPos, direction):
        (boxx, boxy) = boxPos
        (keeperx,keepery) = boxPos
        if (direction == 'w'):
            boxy-=1
            keepery+=1
        elif(direction == 'a'):
            boxx-=1
            keeperx+=1
        elif(direction == 's'):
            boxy+=1
            keepery-=1
        elif(direction == 'd'):
            boxx+=1
            keeperx-=1
        
        if((boxx, boxy) in self.boxes):
            return (False, None)
        
        if((keeperx, keepery)!= boxPos and (keeperx, keepery) in self.boxes):
            return (False, None)

        walls = self.map.filter_tiles([Tiles.WALL])
        
        return ((keeperx, keepery) not in walls and (boxx, boxy) not in walls, (keeperx,keepery))
    
    def goKeeper(self, finalPos, dir):
        tmp = SearchTree(map = self.map, pos = self.keeper, obj= finalPos, boxes = self.boxes)
        return tmp.searchKeeper(finalPos, dir)

    def distToObj(self, objective):
        (x,y) = self.keeper
        (x1,y1) = objective
        return math.sqrt((x-x1)**2 + (y-y1)**2)

    def keeperCanGo(self,direction, canHaveBoxes = False):
        currentPlace = self.map.get_tile(self.keeper)
        if(currentPlace == Tiles.WALL):
            #print("inside wall")
            return (False, "wall!")
        (nextx, nexty) = self.keeper
        if(direction == 'w'):
            nexty-=1
                    
        elif (direction == "a"):
            nextx-=1

        elif(direction == "s"):                
            nexty+=1

        elif(direction == "d"):
            nextx+=1

        if((nextx, nexty) in self.boxes):
            return(canHaveBoxes, (nextx, nexty))

        walls = self.map.filter_tiles([Tiles.WALL])

        return((nextx, nexty) not in walls, (nextx, nexty))

    def boxCanBeMoved(self, boxPos):
        tmp = [self.boxCanGo(boxPos, dir)[0] for dir in ['w','a','s','d']]   
        return True in tmp

class SearchTree:
    def __init__(self,map, pos = None, obj = None, boxes = None):
        self.map = map
        if(boxes == None):
            boxes = map.boxes
        self.root = SearchNode(map.keeper, map, boxes) if pos==None else SearchNode(pos, map, boxes)
        self.solution = []
        self.root.positions = [self.root.keeper]
        self.open = [self.root]
        self.obj = obj
        self.explored = []
        self.exploredDict = {}


    def searchKeeper(self, finalPos, directionToPush):
        if(self.root.map.get_tile(finalPos) == Tiles.WALL):
            return (False, None, None, None)
        (x,y) = finalPos
        if(directionToPush == 'w'):
            y-=1
        elif(directionToPush == 'a'):
            x-=1
        elif(directionToPush == 's'):
            y+=1
        elif(directionToPush == 'd'):
            x+=1
        firstPosOfBox = (x,y) 
        while(self.open):
            node = self.open.pop(0)
            finalBoxes = node.boxes[:]
            if(node.keeper == finalPos):
                for i in range(len(finalBoxes)):
                    if(finalBoxes[i] == firstPosOfBox):
                        if(directionToPush == 'w'):
                            (x,y) = finalBoxes[i]
                            y-=1
                            finalBoxes[i] = (x,y)
                            return (True, node.way + [directionToPush], node.positions + [firstPosOfBox], finalBoxes)
                        elif (directionToPush == 'a'):
                            (x,y) = finalBoxes[i]
                            x-=1
                            finalBoxes[i] = (x,y)
                            return (True, node.way + [directionToPush], node.positions + [firstPosOfBox], finalBoxes)
                        elif (directionToPush == 's'):
                            (x,y) = finalBoxes[i]
                            y+=1
                            finalBoxes[i] = (x,y)
                            return (True, node.way + [directionToPush], node.positions + [firstPosOfBox], finalBoxes)
                        elif (directionToPush == 'd'):
                            (x,y) = finalBoxes[i]
                            x+=1
                            finalBoxes[i] = (x,y)
                            return (True, node.way + [directionToPush], node.positions + [firstPosOfBox], finalBoxes)


            lnew = []
            for dir in ['w','a','s','d']:
                tmp = node.keeperCanGo(dir)
                if(tmp[0] and tmp[1] not in node.positions):
                    newnode = SearchNode(tmp[1], node.map)
                    newnode.keeper = tmp[1]
                    newnode.cost = node.cost + 1
                    newnode.positions = node.positions + [tmp[1]]
                    newnode.way = node.way + [dir]
                    newnode.boxes = node.boxes[:]
                    lnew.append(newnode)
            self.addToOpenKeeper(lnew)
        return(False, None, None, None)

    def addToOpenKeeper(self, list):
        self.open+=list
        self.open.sort(key = lambda x: x.distToObj(self.obj))

    async def search(self):
        print("search")
        await asyncio.sleep(0.0)
        while(self.open):
            keys = list(self.exploredDict.keys())
            node = self.open.pop(0)
            posHash = hash(node.keeper)
            positionExplored = posHash in keys
            boxHashes =hash(frozenset(node.boxes))
            
            if(positionExplored):
                if(boxHashes in self.exploredDict[posHash]):
                    continue
            
            if(node.done()):
                self.solution = node.way
                self.positionsThere = node.positions

                return node.way

            lnewnodes = []
            
                        
            for b in node.boxes:
                
                directions = ['w', 'a','s','d']
                for direction in directions:
                    await asyncio.sleep(0.0)
                    (cango, keeperPos) = node.boxCanGo(boxPos = b, direction = direction)
                    
                                        
                    if(cango):
                        await asyncio.sleep(0.0)
                        (can, wayThere, positions, finalBoxPositions) = node.goKeeper(keeperPos, direction)

                        if(can):
                            toAdd = SearchNode(positions[-1], node.map)
                            toAdd.way= node.way+wayThere 
                            toAdd.cost= node.cost + len(wayThere)  
                            toAdd.boxes = finalBoxPositions[:]
                            pos = hash(toAdd.keeper)
                            newboxhash = hash(frozenset(toAdd.boxes))
                            
                            if(pos in keys):
                                if(newboxhash in self.exploredDict[pos]):
                                    continue

                            tmp = [toAdd.boxCanBeMoved(b) for b in toAdd.boxes]

                            if(True not in tmp and not toAdd.done()):
                                if(pos in keys):
                                    self.exploredDict[pos].append(newboxhash)
                                else:
                                    self.exploredDict[pos] = [newboxhash]
                                continue
                            

                            lnewnodes.append(toAdd)
            self.addToOpenBoxes(lnewnodes)
            if(positionExplored):
                self.exploredDict[posHash].append(boxHashes)
            else:
                self.exploredDict[posHash] = [boxHashes]

                            
    def addToOpenBoxes(self, lnewnodes):
        self.open+=lnewnodes
        self.open.sort(key = lambda x: x.cost)

async def solver(puzzle, solution):
    while True:
        game_properties = await puzzle.get()
        mapa = Map(game_properties["map"])
        print(mapa)

        while True:
            await asyncio.sleep(0.0)  # this should be 0 in your code and this is REQUIRED
            break

        
        toSolve = SearchTree(mapa)

        keys = await toSolve.search()
        print(keys)
        await solution.put(keys)

async def agent_loop(puzzle, solution, server_address="localhost:8000", agent_name="student"):
    async with websockets.connect(f"ws://{server_address}/player") as websocket:

        # Receive information about static game properties
        await websocket.send(json.dumps({"cmd": "join", "name": agent_name}))

        while True:
            try:
                update = json.loads(
                    await websocket.recv()
                )  # receive game update, this must be called timely or your game will get out of sync with the server

                if "map" in update:
                    # we got a new level
                    game_properties = update
                    keys = ""
                    await puzzle.put(game_properties)

                if not solution.empty():
                    keys = await solution.get()

                key = ""
                if len(keys):  # we got a solution!
                    key = keys[0]
                    keys = keys[1:]

                await websocket.send(
                    json.dumps({"cmd": "key", "key": key})
                )
                await asyncio.sleep(0.0)

            except websockets.exceptions.ConnectionClosedOK:
                print("Server has cleanly disconnected us")
                return

# DO NOT CHANGE THE LINES BELLOW
# You can change the default values using the command line, example:
# $ NAME='arrumador' python3 client.py
loop = asyncio.get_event_loop()
SERVER = os.environ.get("SERVER", "localhost")
PORT = os.environ.get("PORT", "8000")
NAME = os.environ.get("NAME", getpass.getuser())

puzzle = asyncio.Queue(loop=loop)
solution = asyncio.Queue(loop=loop)

net_task = loop.create_task(agent_loop(puzzle, solution, f"{SERVER}:{PORT}", NAME))
solver_task = loop.create_task(solver(puzzle, solution))

loop.run_until_complete(asyncio.gather(net_task, solver_task))
loop.close()