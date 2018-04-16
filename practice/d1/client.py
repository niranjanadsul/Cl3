import socket               # Import socket module
import sha

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
message=s.recv(1024)
print str(message)
msgD=s.recv(1024)
print str(msgD)
sh=sha.sha1(message)
sh.process_data()
msgD1=sh.sha_1()
print msgD1
if msgD==msgD1:
	print "message is integrate."
elif msgD != msgD1:
	print "message not integrate"
s.close
