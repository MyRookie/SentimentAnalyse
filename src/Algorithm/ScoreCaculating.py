import math
import sys

sys.path.append('..')
import Analyse.AFX as AFX

class State:
	def __init__(self):
		self.SenShifterState = True
		self.MoodStrength = 1.0
		self.positive = 0.0
		self.negative = 0.0
	def Process(self, score):
		if self.SenShifterState is True:
			self.positive += score
		else:
			self.negative += score

	def Clear(self):
		self.SenShifterState = True
		self.MoodStrength = 1.0
		self.positive = 0.0
		self.negative = 0.0
	def ChangeMood(self,mood):
		if mood.startswith('I'):
			self.MoodStrength *= 2
		if mood.startswith('D'):
			self.MoodStrength /= 2
	def returnScore(self):
		score = self.positive - self.negative
		score *= self.MoodStrength

		return score



#calulating the score pf specific sentence
def CaculateASentence(Sentence):

	S = State()

	for word in Sentence:
		tag = AFX.GetWord(word,'Tag')
		#if the word has no orientation or it is a boring word, just ignore it
		if tag == 0.0 or tag is "Bor":
			continue
		if tag is "Con":
			S.Clear()
		elif tag is "Neg":
			#if there is a negative tagged here, change the state of Sentiment Shifter
			S.SenShifterState = -S.SenShifterState
		elif tag is "Inc" or tag is "Dow":
			S.ChangeMood(tag)
		else:
			S.Process(tag)

	return S.returnScore()


#caculating the score of the Document with specific rules
def Run(Data):
	ScoreList = []
	counter = 0
	for Sen in Data:
		if Sen != []:
			if AFX.GetWord(Sen[0],'Tag') is "Con":
				word = AFX.GetWord(Sen[0],'Word')
			print Sen
			print CaculateASentence(Sen)
		++counter
	pass


#Most people don't like rainy, even if I like the weather quite much.
