from bitstring import BitArray
from math import log,ceil
from flask import Flask,render_template,request

app=Flask(__name__)

def bitcal(m):
	return int(ceil(log(m+1,2)))

def booth(a,b):
	#a multiplicand
	#b multiplier
	#calculate count of bits in multiplier
	count=bitcal(b)
	print "count ",count
	mA=BitArray(uint=a,length=8) #multiplicand
	print "Multiplicand is "
	print mA.bin
	'''
	mAA=BitArray(uint=-a,length=8)
	print mAA.int
	print mAA.bin
	'''
	mB=BitArray(uint=b,length=8) #multiplier
	print "Multiplier is "
	print mB.bin
	
	AC=BitArray(uint=0,length=8)
	QR=mB
	Q1=BitArray(uint=0,length=1)
	Q2=Q1
	print AC.bin," ",QR.bin," ",Q1.bin
	print ""
	for i in range(0,8):	
		if QR[7]==Q1[0]:
			#print "hi"
			Q1[0]=QR[7]
			QR=QR>>1
			QR[0]=AC[7]
			Q2[0]=AC[0]
			AC=AC>>1
			AC[0]=Q2[0]
			print AC.bin," ",QR.bin," ",Q1.bin," Right shift"
		elif QR[7]>Q1[0]:
			AC.int=AC.int-mA.int
			print AC.bin," ",QR.bin," ",Q1.bin," AC-M"
			Q1[0]=QR[7]
			QR=QR>>1
			QR[0]=AC[7]
			Q2[0]=AC[0]
			AC=AC>>1
			AC[0]=Q2[0]
			print AC.bin," ",QR.bin," ",Q1.bin," right shift"
		elif QR[7]<Q1[0]:
			A=AC.int+mA.int
			AC=BitArray(uint=A,length=8)
			print AC.bin," ",QR.bin," ",Q1.bin," AC+M"
			Q1[0]=QR[7]
			QR=QR>>1
			QR[0]=AC[7]
			Q2[0]=AC[0]
			AC=AC>>1
			AC[0]=Q2[0]
			print AC.bin," ",QR.bin," ",Q1.bin," right shift"
		
	AC=AC+QR
	#print AC.bin
	product=AC.int
	#print "product"
	#print product
	return product,AC.bin 

#function to render html template
@app.route('/')
def r():
	return render_template('h.html')		

@app.route('/',methods=['POST'])		
def i():
	a=int(request.form['text1'])
	b=int(request.form['text2'])
	n,m=booth(a,b)
	return "Answer is "+str(n)
#booth(6,6)
if __name__=='__main__':
	app.run('localhost',debug=True)
