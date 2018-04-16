from __future__ import division
import string
from flask import Flask,render_template,request

app=Flask(__name__)

class plaga:
	data=None
	def __init__(self,dt):
		self.data=plaga.process(dt)

	@staticmethod
	def process(txt):
		#we remove punctuation marks from the text and convert string into set
		for i in list(string.punctuation+'\n'):
			txt=txt.replace(i,' ')
		return set(txt.lower().strip().split(' '))-set([''])

	def check(self,txt):
		txt1=plaga.process(txt)
		lenp=len(txt1 & self.data) #intersection of two sets
		return lenp/len(txt1)

text="hello\nI am an engineering student\n"
p=plaga(text)

@app.route('/')
def ren():
	return render_template("h.html")

@app.route('/',methods=['POST'])
def plagcheck():
	txt=request.form['value']
	global p
	sc=p.check(txt)
	response="Processing the text<br>"
	response+="plag score is "+str(sc)
	return (response)

if __name__=="__main__":
	app.run("localhost",debug=True)
