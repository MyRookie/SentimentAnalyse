from nltk.corpus import wordnet
import json
import os

punctuation = [',','.','?','!',';']
SentimentShifter = {}
Conjunction = {}

#Check whether the string is a word
def isWord(s):
	if s[0] >= 'a' and s[0] <= 'z':
		return True;
	return False;

#convent list to dictionaries
def GetWord(word,Cmd):
	return {
		'Word':word[0],
		'PoS':word[1],
		'Tag':word[2],
	}.get(Cmd,None)

#extract the data from WordNet
def WordNetInfo(synset):
	return unicode(synset).split('.')

#convent Part of Speech to wordnet format
def PoSConvent(PoS):
	if PoS.startswith('J'):
		return wordnet.ADJ
	elif PoS.startswith('V'):
		return wordnet.VERB
	elif PoS.startswith('N'):
		return wordnet.NOUN
	elif PoS.startswith('R'):
		return wordnet.ADV
	else:
		return PoS

#Check if the PoS of word in document match the selected gloss
def GetWordNetPoS(word,notation,PoS):
	for i in wordnet.synsets(word):
		if WordNetInfo(i.name())[0] == word and WordNetInfo(i.name())[2] == notation and PoS == i.pos():
			return True
	return False

#read json file
def ConventJson():
	if not open('../Profile/SentimentShifter.json','r'):
		print "File Not Found"
		return None
	#open the SentimentShifter.json to get the negation and increment
	with open('../Profile/SentimentShifter.json','r') as f:
		data = json.load(f)

		negation = data.get('negation', None)
		if negation is not None:
			for element in data['negation']:
				for key in element:
					SentimentShifter[key] = "Neg"
		increment = data.get('increment', None)
		if increment is not None:
			for element in data['increment']:
				for key in element:
					SentimentShifter[key] = "Inc"
		downtoner = data.get('downtoner',None)
		if downtoner is not None:
			for element in data['downtoner']:
				for key in element:
					SentimentShifter[key] = "Dow"

	
	if not open('../Profile/Conjunction.json','r'):
		print "File Not Found"
		return None
	#open the Conjunction.json to get the conjunctions
	with open('../Profile/Conjunction.json','r') as f:
		data = json.load(f)

		conjunction = data.get('conjunction',None)
		if conjunction is not None:
			for element in data['conjunction']:
				for key in element:
					Conjunction[key] = element[key]



		


	

