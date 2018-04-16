class crypt:
	key=""

	def __init__(self,data):
		crypt.key=data.upper()
		
	def vignere(self,msg,mode):
		if mode not in('d','e'):
			print "Enter the mode as d or e"
			mode=raw_input()
		msg=msg.upper()
		cipher=""
		key_int=[ord(crypt.key[i]) for i in range(0,len(crypt.key))]
		msg_int=[ord(msg[i]) for i in range(0,len(msg))]
		#print msg
		#print msg_int
		#print crypt.key
		#print key_int
		if mode=='d':
			for i in range(0,len(msg_int)):
				v=(msg_int[i]-key_int[i%len(key_int)]) % 26
				#print v
				cipher+=chr(v + 65)
		if mode=='e':	
			for i in range(0,len(msg_int)):
				v=(msg_int[i]+key_int[i%len(key_int)]) % 26
				#print v
				cipher+=chr(v + 65)	
		return cipher			
	
	def caeser(self,msg,mode):
		if mode not in('d','e'):
			print "Enter the mode as d or e"
			mode=raw_input()
		msg=msg.upper()
		cipher=""
		#key_int=[ord(crypt.key[i]) for i in range(0,len(crypt.key))]
		msg_int=[ord(msg[i]) for i in range(0,len(msg))]
		print msg
		print msg_int
		#print crypt.key
		#print key_int
		if mode=='d':
			for i in range(0,len(msg_int)):
				v=(msg_int[i]-3)
				print v
				if v<65:
					v+=26
				cipher+=chr(v)
		if mode=='e':	
			for i in range(0,len(msg_int)):
				v=(msg_int[i]+3) 
				print v
				if v>90:
					v-=26 
				cipher+=chr(v)	
		return cipher		
c=crypt(raw_input("Enter the key"))
ciphr=c.vignere(raw_input("enter the text to encrypt"),"e")
print ciphr
print c.vignere(ciphr,"d")
ciphr=c.caeser(raw_input("enter the text to encrypt"),"e")
print ciphr
print c.caeser(ciphr,"d")


