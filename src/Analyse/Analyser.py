# This is the analyser of the project which is called directly by the main function
# The return value of this function is the Score of the document sentiment

import sys
import SentiWordNet
import DocProcessing
import nltk
import AFX

from stop_words import get_stop_words

#change the path to import the file
sys.path.append('..')
import Algorithm.CosSimilarity as CS
import Algorithm.ScoreCaculating as Caculator


#path of the SentiWordNet
path = "../Library/SentiWordNet_3.0.txt"

#return the type of the word: sentiment shifter/stop words/conjunction/sentiment words)
def ProcessWord(word):
	#check negation/increment/downtoner words first
	if AFX.SentimentShifter.has_key(word) is True:
		return AFX.SentimentShifter[word]
	#than mark if it is a conjunction
	if AFX.Conjunction.has_key(word) is True:
		return "Con"
	#check the stop words tag
	if word in get_stop_words('english'):
		return "Bor"
	
#convent the sentence into expression and add tags on it
#At here Every word is define as a triple Tuple (word,PoS,Tag)
def GenerateExpression(theList):
	Expression = []
	for Sentence in theList:
		SentenceBuffer = []
		for word in Sentence:
			tag = ProcessWord(AFX.GetWord(word,'Word'))
			WordTuple = (AFX.GetWord(word,'Word'),AFX.GetWord(word,'PoS'),tag)
			SentenceBuffer.append(WordTuple)
		Expression.append(SentenceBuffer)

	return Expression

def ProcessGloss(st):
	Gloss = nltk.pos_tag(nltk.word_tokenize(st))
	Expression = GenerateExpression(Punctuate(Gloss))
	return Expression

#Add orientation to the rest of words which hasn't been tagged
def AddScore(Expression):
	DocData = []
	for sentence in Expression:
		Sen = []
		for word in sentence:
			if AFX.GetWord(word,'Tag') is not None:
				Sen.append((AFX.GetWord(word,'Word'),AFX.GetWord(word,'PoS'),AFX.GetWord(word,'Tag')))
				continue
			else:
				# print "For word: " + AFX.GetWord(word,'Word')
				# print word
				gloss = SentiWordNet.return_all_gloss(path, AFX.GetWord(word,'Word') , AFX.GetWord(word,'PoS'))
				CosSim = (-1,"")
				for key in gloss:
					GlossExp = ProcessGloss(key)
					v = CS.Caculate(GlossExp,Expression)
					if CosSim[0] < v:
						CosSim = (v,key)
				if CosSim[1] is '':
					print word
					continue
				Sen.append((AFX.GetWord(word,'Word'),AFX.GetWord(word,'PoS'),gloss[CosSim[1]]))
		DocData.append(Sen)

	return DocData

#divide the sentence and different words
def Punctuate(list):
	#List contains all the words in the document
	#Buff is a buffer which save the temporary data 
	List = []
	Buff = []

	for w in list:
		if w[0] in AFX.punctuation:
			if w[0] == AFX.punctuation[0]:
				continue;
			List.append(Buff)
			Buff = []
		else:

			Buff.append((w[0].lower(),AFX.PoSConvent(w[1]),None))
	#if the sentence ended unexpectly, add the last sentence in the list
	if Buff is not []:
		List.append(Buff)

	return List

def Run(str):

	#read data about conjunction/sentiment shifters from file
	AFX.ConventJson()
	#pre-process of the sentences including Punctuation, Mark sentiment shifter, 
	#Mark conjunctions, remove boring words and transform the sentance to a list
	SentenceWithPoS = nltk.pos_tag(nltk.word_tokenize(str))
	WordList = Punctuate(SentenceWithPoS)
	Expression = GenerateExpression(WordList)
	#give orientation to words which doesn't belong to Conjunction/Stop words and Sentiment shifters
	Data = AddScore(Expression)
	Caculator.Run(Data)



#Most people don't like rainy, even though I like the weather quite much.


