import unittest
import threading
import xml.etree.ElementTree as et
class BQ(unittest.TestCase):
	
	def set_list(self,fil):
		tree=et.parse(fil)
		root=tree.getroot()
		self.data=[int(x) for x in root.text.strip().split(' ')]
		return self.data
	
	def bS(self,key):
		return self.bSearch(0,len(self.data)-1,key)

	def bSearch(self,low,high,key):
		if low > high:
			return -1
		mid=(low+high)/2
		if self.data[mid]==key:
			return mid
		elif key<self.data[mid]:
			return self.bSearch(low,mid-1,key)
		elif key>self.data[mid]:
			return self.bSearch(mid+1,high,key)
				
	
	def swap(self,i,j):
		assert(i<len(self.data) and j<len(self.data)),"Index out of bound"
		temp=self.data[i]
		self.data[i]=self.data[j]
		self.data[j]=temp

	def partition(self,low,high):
		pivot=self.data[high]
		i=low-1
		for j in range(low,high):
			if self.data[j]<=pivot:
				i+=1
				self.swap(i,j)
		self.swap(i+1,high)
		#print self.data
		return i+1		

	def qkSort(self,low,high):
		if low>high:
			return
		split=self.partition(low,high)
		threading.Thread(self.qkSort(low,split-1)).start()
		threading.Thread(self.qkSort(split+1,high)).start() 	
	
	def qSort(self):
		self.qkSort(0,len(self.data)-1)
		print self.data
		
	def test_reader(self):
		self.assertEqual(self.set_list("h.xml"),[10, 20, 30, 11, 12])	
		self.assertRaises(IOError,lambda : self.set_list("h1.xml"))

	def test_swap(self):
		self.data=[1, 2, 3]
		self.swap(1,2)
		self.assertEqual(self.data,[1, 3, 2])

	def test_part(self):
		self.data=[1, 3, 2]
		self.assertEqual(self.partition(0,2),1)

	

	def runTest(self):
		pass

b=BQ()
l=b.set_list("h.xml")
print l
b.qSort()
val=b.bS(int(raw_input("enter the key to search ")))
print "element found at index ",val

#unit test for opening xml
b.test_reader()
b.test_swap()
b.test_part()
if __name__=='__main__':
	unittest.main()
