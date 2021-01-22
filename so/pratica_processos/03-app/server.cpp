/*
id = getPendingRequest()           //take a buffer from pending requests fifo
req = getRequestData(id)           // take the request
resp = produceResponse(req)        //produce a response
putResponseData(resp, id)          //put response data on buffer
signalResponseIsAvailable(id)      // client is woken up
*/

