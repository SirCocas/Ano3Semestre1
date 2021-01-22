/*
id = getFreeBuffer()       //take buffer from free buffers fifo
putRequestData(data, id)   //put request data on buffer
addNewPendingRequest(id);  //add buffer to pending requests fifo
waitForResponse(id)        //wait (blocked) until a response is available
resp = getResponseData(id) //get response from buffer
releaseBuffer(id)          //buffer is free, so add it fto free buffers fifo
*/

#include  "fifo.h"
#include  "delays.h"
#include  "process.h"


int getFreeBuffer(void){
    fifoConnect();
    unsigned int pid, value;
    while(1)
    {
        /* do something else */
        gaussianDelay(10, 5);

        /* retrieve an item from the fifo */
        fifoOut(&pid, &value);

        if (value == 99999999)
            break;
        
        fifoIn(pid, value);    //put them back in
    }

    /* disconnect from the FIFO */
    fifoDisconnect();
    return pid;

}


int main(void){
    int id = getFreeBuffer();
    return 0;
}