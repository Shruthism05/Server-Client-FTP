""" 
This is the server script - server.py which will accept the file from client and save it 
in the server location
"""
import socket 

server_socket = socket.socket()

port = 12345

server_socket.bind(('',port)) #'' reprsents INADDR_ANY
print "the socket descriptor is %d" %(server_socket.fileno())
print "socket bound to %s" %(port)

server_socket.listen(5)
print "socket listening for a max of 5 simultaneous connections"

while True:
    conn, addr = server_socket.accept()
    file_to_write = conn.recv(1024)
    conn.send("done") #send acknowledgement to client
    print "Writing to file {}".format(file_to_write)
    try:
        with open(file_to_write,"wb") as file_to_be_saved: 
            data_recieved_from_client = conn.recv(1024)
            while(data_recieved_from_client != "EOF" and len(data_recieved_from_client)):
                print(data_recieved_from_client)
                file_to_be_saved.write(data_recieved_from_client)
                conn.send("done")
                data_recieved_from_client = conn.recv(1024)

        print "Finished reading and writing file data from server"
        print "Got connection request from ",addr

        conn.send("THIS IS RESPONSE FROM SERVER!!")
    
        conn.close()
    except IOError as (errno,strerror):
        print "I/O error({0}): {1}".format(errno, strerror)

server_socket.close()
