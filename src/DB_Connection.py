from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.fb

for a in db.feedbacks.find():
	print a