

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2020
# v1.9 - 2019/10/20
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#
import collections
from collections import Counter

class Relation:
    def __init__(self,e1,rel,e2):
        self.entity1 = e1
#       self.relation = rel  # obsoleto
        self.name = rel
        self.entity2 = e2
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + \
               str(self.entity2) + ")"
    def __repr__(self):
        return str(self)


class AssocOne(Relation):
    def __init__(self, e1,assoc, e2):
        Relation.__init__(self, e1, assoc, e2)

class AssocNum(Relation):
    def __init__(self, e1, assoc, e2):
        Relation.__init__(self, e1, assoc, e2)


# Subclasse Association
class Association(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,sub,super):
        Relation.__init__(self,sub,"subtype",super)


#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        Relation.__init__(self,obj,"member",type)

#   Exemplo:
#   m = Member('socrates','homem')

# classe Declaration
# -- associa um utilizador a uma relacao por si inserida
#    na rede semantica
#
class Declaration:
    def __init__(self,user,rel):
        self.user = user
        self.relation = rel
    def __str__(self):
        return "decl("+str(self.user)+","+str(self.relation)+")"
    def __repr__(self):
        return str(self)

#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self,ldecl=None):
        self.declarations = [] if ldecl==None else ldecl
    def __str__(self):
        return my_list2string(self.declarations)
    def insert(self,decl):
        self.declarations.append(decl)
    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result
    def show_query_result(self):
        for d in self.query_result:
            print(str(d))

    def list_associations(self):
        result = [ d.relation.name for d in self.declarations if isinstance(d.relation, Association)]
        return list(set(result))

    def list_objects(self):
        result = [ d.relation.entity1 for d in self.declarations if isinstance(d.relation, Member)]
        return list(set(result))

    def list_users(self):
        result = [d.user for d in self.query_local()]
        return list(set(result))

    def list_types(self):
        result = [d.relation.entity2 for d in self.declarations if isinstance(d.relation, Subtype) or isinstance(d.relation, Member)]
        otherRes = [d.relation.entity1 for d in self.declarations if isinstance(d.relation, Subtype)]
        otherRes+=result
        return list(set(otherRes))

    def list_local_associations(self, userGiven):
        result = [ d.relation.name for d in self.query_local(e1 = userGiven) if isinstance(d.relation, Association)]
        return list(set(result))

    def list_relations_by_user(self, userGiven):
        result = [d.relation.name for d in self.query_local(user=userGiven)]
        return list(set(result))

    def associations_by_user(self,userGiven):
        result = [ d.relation.name for d in self.query_local(user = userGiven) if not isinstance(d.relation, Member) and not isinstance(d.relation, Subtype)]
        return len(set(result))

    def list_local_associations_by_user(self, userGiven):
        result = [ (d.relation.name, d.user) for d in self.query_local(e1 = userGiven) if isinstance(d.relation, Association)]
        return list(set(result))

    def predecessor(self, upper, lower):
       parents = [d.relation.entity2 for d in self.declarations if not isinstance(d.relation, Association) and d.relation.entity1 == lower]
       for p in parents:
            if p == upper:
               return True
            if self.predecessor(upper, p):
               return True
       return False
    
    def predecessor_path(self, upper, lower):
        parents = [d.relation.entity2 for d in self.declarations if not isinstance(d.relation, Association) and d.relation.entity1 == lower]
        for p in parents:
            if p == upper :
                return [upper, lower]
            pathUP = self.predecessor_path(upper, p)
            if pathUP!= None:
                return pathUP + [lower]   #lower == p
        return None


    def query(self, entity, assertion=None):
        parents = [d.relation.entity2 for d in self.query_local(e1 = entity)]

        ldecl = [d for d in self.query_local(e1 = entity, rel = assertion) if isinstance(d.relation, Association)]

        for p in parents:
            ldecl+= self.query(p, assertion)

        return ldecl

    def query2(self, entity, assertion = None):
        tmp = self.query(entity, assertion)
        others = [d for d in self.query_local(e1 = entity, rel = assertion) if isinstance(d.relation, Member) or isinstance(d.relation, Subtype)]
        return tmp + others

    def query_cancel(self, entity, assertion):
        ldecl = [d for d in self.query_local(e1 = entity, rel = assertion) if isinstance(d.relation, Association)]

        if (ldecl == []):
            parents = [d.relation.entity2 for d in self.query_local(e1 = entity) if not isinstance(d.relation, Association)]

            for p in parents:
                ldecl+= self.query_cancel(p, assertion)

        return ldecl

    def query_down(self, type, association, first = True):

        ldecl = [] if first else [ d for d in self.query_local(e1 = type, rel = association) if isinstance(d.relation, Association)]

        children = [d.relation.entity1 for d in self.query_local(e2 = type) if not isinstance(d.relation, Association)]


        for c in children:
            ldecl+= self.query_down(c,association, False)
        
        return ldecl

    def query_induce(self, type, association):
        ldecl = self.query_down(type, association)
        values = [d.relation.entity2 for d in ldecl]
        currentBest = values[0]
        currentMost = values.count(values[0])

        for item in values:
            if(values.count(item)> currentMost):
                currentMost = values.count(item)
                currentBest = item
        return currentBest


    def query_local_assoc(self, entity, association):
        decl = self.query_local(e1 = entity, rel = association)
        values = [d.relation.entity2 for d in decl]
        val_freqs = Counter(values)
        if isinstance(decl[0], Association) or isinstance(decl[0].relation, Association):
            toRet = []
            comm = val_freqs.most_common()
            summ = 0.0
            while(summ<0.75 and comm):
                tmp = comm.pop(0)
                perc = (tmp[1]+0.0)/len(values)
                summ += perc
                toRet.append((tmp[0], perc))
            return toRet
        elif isinstance(decl[0], AssocOne) or isinstance(decl[0].relation, AssocOne):
            tmp = val_freqs.most_common()
            return (tmp[0][0], tmp[0][1]/len(values))
        elif isinstance(decl[0], AssocNum) or isinstance(decl[0].relation, AssocNum):
            val = 0
            for v in values:
                val+=v
            return val/len(values)

    def query_assoc_value(self, entity, association):
        decl = self.query_local(e1 = entity, rel = association)
        values = [d.relation.entity2 for d in decl]
        #check if all are the same
        if(decl and all(d.relation.entity2 == values[0] for d in decl)):  
            return values[0]

        tmp = [d for d in self.query(entity, association)]
        valuesAll = [d.relation.entity2 for d in tmp]
        counterLocal = Counter(values)
        print(valuesAll)
        #check if there is heritage
        if(not valuesAll):
            return counterLocal.most_common()[0][0]

        counterAll = Counter(valuesAll)
        currentMin = None
        currentV = None
        for k in counterAll.most_common():
            key = k[0]
            if(currentMin == None):
                currentMin = counterLocal[key] + counterAll[key]
                currentV = key
            else:
                tmp = counterLocal[key] + counterAll[key]
                if(tmp>currentMin):
                    currentMin = tmp
                    currentV = key
        return currentV


        

# Funcao auxiliar para converter para cadeias de caracteres
# listas cujos elementos sejam convertiveis para
# cadeias de caracteres
def my_list2string(list):
   if list == []:
       return "[]"
   s = "[ " + str(list[0])
   for i in range(1,len(list)):
       s += ", " + str(list[i])
   return s + " ]"
    

