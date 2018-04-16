class sha1:
	data=""
	bytes=""	

	def __init__(self,data):
		sha1.data=data
		self.a=0x67452301
		self.b=0xEFCDAB89
		self.c=0x98BADCFE
		self.d=0x10325476
		self.e=0xC3D2E1F0
		sha1.bytes=""		

	def process_data(self):
		for i in range(0,len(self.data)):
			sha1.bytes+='{0:08b}'.format(ord(sha1.data[i])) #convert string to binary 
								   # ord("A")=65
		length=len(sha1.bytes)
		print length
		#now append '10000000' bit to string
		sha1.bytes+="1"#'{0:08b}'.format(128)
		#append '0' bits till len is 448 % 512
		while len(sha1.bytes)%512 !=448:
			sha1.bytes+="0"#'{0:08b}'.format(0)
		# data has been padded 
		#padd the length of the data to last
		sha1.bytes+='{0:064b}'.format(length)	
	# lets divide the data into chunks 
		
	def chunks(self,d11,n):
		return [d11[i:i+n] for i in range(0,len(d11),n)]   
	#returns chunks from d of length n		

	#lets write the rotate left logic
	def rol(self,d11,n):
		return ((d11<<n) | (d11>>(32-n))) & 0xffffffff
	
	#lets define the keys needed for the 80 rounds and start each round 
	def sha_1(self):
		#get chunks of 512 bits
		for c11 in self.chunks(sha1.bytes,512):
			a1=self.a
			b1=self.b
			c1=self.c
			d1=self.d
			e1=self.e
			#define 16 keys each 32 bit
			w=[0]*80
			words=self.chunks(c11,32)
			#print words
			#print w
			for j in range(0,16):
				w[j]=int(words[j],2) # take as binary and convert to decimal
			#remaining 16 to 80 keys are created below
			for i in range(16,80):
				w[i]= self.rol((w[i-3]^w[i-8]^w[i-14]^w[i-16]),1)
			#key are ready
			#lets define the fiestel function and perform the 80 rounds
			for i in range(0,80):
				if 0<=i<=19:
					f=(b1 & c1) | ((~b1) & d1)
					k=0x5A827999
				elif 20<=i<=39:
					f=b1 ^ c1 ^ d1
					k=0x6ED9EBA1
				elif 40<=i<=59:
					f=(b1 & c1)|(b1 & d1)|(c1 & d1)
					k=0x8F1BBCDC
				elif 60<=i<=79:
					f=b1 ^ c1 ^ d1
					k=0xCA62C1D6
			
				#sum32 logic
				temp=self.rol(a1,5)+ f + e1 + k + w[i] & 0xffffffff
				e1=d1
				d1=c1
				c1=self.rol(b1,30)
				b1=a1
				a1=temp
			self.a=self.a+a1 & 0xffffffff
			self.b=self.b+b1 & 0xffffffff
			self.c=self.c+c1 & 0xffffffff
			self.d=self.d+d1 & 0xffffffff
			self.e=self.e+e1 & 0xffffffff
		return '%08x%08x%08x%08x%08x' % (self.a, self.b, self.c, self.d, self.e)
'''
sh=sha1(raw_input())
sh.process_data()
print(sh.sha_1())
'''	
