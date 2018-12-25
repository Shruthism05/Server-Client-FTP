""" 
This is client script - client.py attempting to send a txt file 
to the server - server.py 
"""
import socket
import constant

'''
[Name] : read_write_synchronize_check()
[Arguments] : s - socket instance

implementing custom client-server read write  synchronization, since send() by default doesnt block itself.
call read_write_synchronize_check() after every send() made to server if send() needs to wait for acknowledgement from server
'''
def read_write_synchronize_check(s):
    done = ""
    done = s.recv(1024)
    while(done != "done"):
        done = s.recv(1024)
        pass 

s = socket.socket()
file_to_send = open(constant.FILE_TO_SEND, "rb")
#print(file_to_send)
port = 12345

s.connect(('127.0.0.1', port)) #'127.0.0.1' is the loopback address
s.send(constant.FILE_TO_SEND) #send file name to server
read_write_synchronize_check(s) #wait for acknowledgement from server
data_read = file_to_send.read(1024)


#keep looping till we have finished reading data from our file
while(len(data_read)):
    s.send(data_read)
    read_write_synchronize_check(s)
    data_read = file_to_send.read(1024)

EOF = "EOF" #send "" to server to indicate EOF
s.send(EOF)
print(data_read)
file_to_send.close()
print s.recv(1024)

s.close()
