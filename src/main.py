#!/usr/bin/python3

from flask import Flask
from flask import request

import Analyse.AnalyseSentiment
import Analyse.Analyser

# client = MongoClient('mongodb://localhost:27017/')
# db = client.fb


app = Flask(__name__)

@app.route("/connect", methods = ['GET','POST'])
def display():
	if request.method == 'POST':
		#Analyse.AnalyseSentiment.Run(request.form['0'])
		#recieve the document from client and process the document with Analyser
		document = request.form['0']
		Analyse.Analyser.Run(document)
		#save the data to database first
		#db.feedbacks.insert({'tag':0,'text':var})

	else:
		print 'connected'
	return "connected"

app.debug = True



if __name__ == "__main__":
    app.run(host='127.0.0.1')

# import DataAnalysing
# anly = DataAnalysing.Analysing()
# anly.analyse(var)