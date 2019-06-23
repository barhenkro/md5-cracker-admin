# md5-cracker-admin
An admin server that communicates with cracker at the network to crack the origin imput of a md5's result. The server spilts the possible options between the connected client computers

## Requirements
* python 2.7

## Prototocol
### Connecting
The client need to send his name as follows:
> name: {name}

Note that there is a space after the colon.

After te server accepted the the client's name it will send a range of possibile values that the client need to check. the message looks as follows:
>start:{starting point},stop:{stopping point},md5:{the result of the md5}



### Finding the origin answer
In case the a client found the origin input of the md5 result he needs to send it to the server as follows:
> found:{answer}

If the answer is indeed correct the server will send to the client who found the answer the message:
> You are the king

And after that will send to every one 
> bye

### Requesting new range
In case the client iterated over the whole range and didn't find the correct answer it needs to request new  range from the server by sending:
> not found

The server will send a new ranage at the same syntax as before:
> start:{starting point},stop:{stopping point},md5:{the result of the md5}

### Keep alive
Once in 3 seconds the client need to send a messgae which indicates that the client is alive. th message looks as follows:
>keep-alive

## Author
* @[animelech](https://github.com/animelech)
* @[shakedzeltzer](https://github.com/shakedzeltzer)
* @[barhenkro](https://github.com/barhenkro)


