import socket               # Import socket module
import sha

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(1)                 # Now wait for client connection.
while True:
	c, addr = s.accept()     # Establish connection with client.
	print 'Got connection from ', addr
	data=raw_input("enter the data to be sent ")
	c.send(data)
	sh=sha.sha1(data)
	sh.process_data()
	msgD=sh.sha_1()
	print msgD
	c.send(msgD)
	data=""
	c.close()                # Close the connection
	
