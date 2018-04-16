from pymongo import MongoClient
#import pprint

connection=MongoClient("localhost",27017)
db=connection.test.diniraw7

post={"ph": int(9146115122),"add":"gondhale nagar"}
db.insert(post)

rec=db.find({"ph":int(9146115122)})
print rec[1]
