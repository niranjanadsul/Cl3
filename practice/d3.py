import random
import math
class Dsa:
	"""docstring for Dsa"""
	def __init__(self,):
		self.p=None
		self.q=None
		self.g=None
		#global public key components G
		self.x=None #private key of sender
		self.y=None #public key of sender
		self.k=None #random key
		self.H=None #hash value of a message

	def isPrime(self,a):
		if a<=1:
			return False
		if a==2:
			return True
		if a%2==0:
			return False
		i=3
		while i<=math.ceil(math.pow(a,0.5)):
			if a%i==0:
				return False
			i+=2
		return True
	
	def mod_pow(self,base,exp,mod):
		ans=1
		for i in range(0,exp):
			ans=(ans*base)%mod
		return ans%mod

	def genG(self): #function to craete Global public key components
		#create a list of prime numbers from 2 to 100
		primeList=[]
		for x in range(4,100):
			if self.isPrime(x):
				primeList.append(x)
		#print  primeList
		#print len(primeList)
		#select one prime number randomly as p
		self.p=random.choice(primeList)
		print "Value of p is ",self.p

		#use greatest prime divisor of p-1 as q
		for i in range(1,self.p-1):
			if (self.p-1)%i==0:
				if self.isPrime(i):
					self.q=i
		print "Value of q is ",self.q

		#now select 1<h<p-1
		h=random.randint(2,self.p-1)
		print "value of h is ",h

		#calculate g
		self.g=self.mod_pow(h,(self.p-1)/self.q,self.p)
		print "value of g is ",self.g

	def genK(self): #function to create private and public keys of the sender and K
		#private key x is a random number 0 < x < q
		self.x=random.randint(1,self.q-1)
		print "private key x is ",self.x

		#public key y
		self.y=self.mod_pow(self.g,self.x,self.p)
		print "value of public key y is ",self.y

		#0 < k < q
		self.k=random.randint(1,self.q-1)
		print "Value of K is ",self.k

	def mod_inv(self,a,b):
		for i in range(1,b):
			if a*i%b==1:
				return i
		raise Exception

	def createSign(self):  
		self.H=int(raw_input("enter the hash value : "))
		#print self.H
		r=self.mod_pow(self.g,self.k,self.p)%self.q
		#function to create signature components s and r
		#hashlib.sha1("Nobody inspects the spammish repetition").hexdigest()
		#int(hashlib.sha1("Nobody inspects the spammish repetition").hexdigest(),16)  16 is base
		print "r component of signature is ",r#int(r)
		kinv=self.mod_inv(self.k,self.q)
		s=((self.H+self.x*r)*kinv)%self.q
		print "s component of signature is ",s#int(s)
		#return int(r),int(s)
		return r,s


	def calW(self,s):
		# w = s^-1 mod q
		z=self.q
		for i in range(1,z):
			if (s*i)%z==1:
				print "got inverse"
				return i
		#print "inverse not got"
		#return 1
		#return pow(int(s),z-2,z)

	def calU1(self,r,s):
		w1=self.calW(s)
		print "w1 ",w1
		return (self.H*w1)%self.q


	def calU2(self,r,s):
			w1=self.calW(s)
			print w1
			return (r*w1)%self.q

	def verifySign(self,r,s):
		u1=self.calU1(r,s)
		u2=self.calU2(r,s)
		return ((math.pow(self.g,u1)*math.pow(self.y,u2))%self.p)%self.q




d=Dsa()
d.genG()
d.genK()
rc,sc=d.createSign()
#print rc,sc
v=d.verifySign(rc,sc)
print "V is ",v
