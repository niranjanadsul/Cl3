import threading
import time
import sys
from pymongo import MongoClient
#we set semaphore with count 4 for avoiding deadlock
#then initialise 5 chopstick
#then we initialise philosopher

client=MongoClient('localhost',27017)
db=client.test.diniraw7

class Semaphore:

	def __init__(self,num):
		self.number=num
		self.lock=threading.Condition(threading.Lock())

	def down(self):
		with self.lock:
			while self.number==0:
				self.lock.wait()
			self.number-=1

	def up(self):
		with self.lock:
			self.number+=1
			self.lock.notify()


class chopStick:

	def __init__(self,num):
		self.id=num #id of chopstick
		self.user=-1 #philosopher using it
		self.taken=False #whether chopstick is taken or not
		self.lock=threading.Condition(threading.Lock())

	def take(self,num):
		with self.lock:
			while self.taken==True:
				self.lock.wait()
			self.taken=True
			self.user=num
			sys.stdout.write("p[%s] took c[%s]\n" % (num, self.id))

	def drop(self,num):
		with self.lock:
			while self.taken==False:
				self.lock.wait()
			self.taken=False
			self.user=-1
			sys.stdout.write("p[%s] dropped c[%s]\n" % (num, self.id))
			self.lock.notifyAll()



class philosopher(threading.Thread):
	def __init__(self,num,l,r,butler):
		threading.Thread.__init__(self)
		self.id=num
		self.left=l
		self.right=r
		self.butler=butler

	def run(self):
		for i in range(20):
			self.butler.down()
			time.sleep(0.1)
			self.left.take(self.id)
			time.sleep(0.1)
			self.right.take(self.id)
			time.sleep(0.1)
			#print "philosopher ",self.id," is eating "
			rec=db.find({'ph':int(9146115122)})
			print("record is ",rec[0])
			self.right.drop(self.id)
			self.left.drop(self.id)
			self.butler.up()

		sys.stdout.write("p[%s] finished thinking and eating\n" % self.id)

def main():
	n=5
	butler=Semaphore(n-1)
	c=[chopStick(i) for i in range(n)]
	p=[philosopher(i,c[i],c[(i+1)%n],butler) for i in range(n)]

	for i in range(0,n):
		p[i].start()


if __name__=='__main__':
	main()


