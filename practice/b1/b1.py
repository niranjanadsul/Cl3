import xml.etree.ElementTree as et
import unittest
class Queen(unittest.TestCase):
	board = []
	size = 0
	
	def runTest(self):
		pass

	def setSize(self,s):
		self.size=s
		self.xmlReader("h.xml")
	
	
	def xmlReader(self,_file):
		tree=et.parse(_file)
		root=tree.getroot()
		x,y=str(root.text).strip().split(' ')
		self.board.append((int(x),int(y)))

	def printBoard(self):
		print self.board

	def isDanger(self,pos1,pos2):
		x1,y1=pos1
		x2,y2=pos2
		if x1==x2 or y1==y2:
			return True
		if x1-y1==x2-y2 or x1+y1==x2+y2:
			return True
		return False
			
	def checkSafe(self,pos1):
		for pos2 in self.board:
			if self.isDanger(pos1,pos2):
				return False
		return True	

	def solveBoard(self,row):
		if row>self.size:
			self.printBoard()
		else:
			for col in range(1,self.size+1):
				if self.checkSafe((row,col)):
					self.board.append((row,col))
					self.solveBoard(row+1)
					self.board.remove((row,col))

	def test_correct(self):
		self.assertTrue(self.isDanger((1,2),(2,3)))

q=Queen()
q.setSize(8)
q.solveBoard(2)

p=Queen()
p.test_correct()


if __name__=='__main__':
	unittest.main()
