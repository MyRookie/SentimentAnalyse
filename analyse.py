import DataAnalysing

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.fb

var = ''

for a in db.feedbacks.find({'tag':0},{'text':1}):
	#print a.get('text')
	var += a.get('text')

	# anly = DataAnalysing.Analysing()
	# anly.analyse(var)

print var
anly = DataAnalysing.Analysing()
thelist = anly.analyse(var)

for v in thelist:
	print v