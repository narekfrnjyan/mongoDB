from pymongo import MongoClient
import json
import pandas as pd
client = MongoClient('localhost', 27017)
db = client.webDB
db
books=db.books
books=list(books.find())
for  doc in books:
    doc["_id"]=str(doc["_id"])
with open("/home/narek/Desktop/test1.json","w") as file:
    file.write("[")
    for i in books:
        json.dump(i,file)
        if books.index(i)<len(books)-1:
            file.write(",")
    file.write("]")
data=pd.read_json("/home/narek/Desktop/test1.json",orient="columns")
data
