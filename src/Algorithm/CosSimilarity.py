import math
import sys

sys.path.append('..')
import Analyse.AFX as AFX

#caculate term frequency
def TermFrequency(List,L):
	dictionary = {}
	Vector = {}
	for w in List:
		if dictionary.has_key(w) is False:
			dictionary[w] = 1
		else:
			dictionary[w] += 1 

	for w in L:
		value = dictionary.get(w,0)
		Vector[w] = value

	return Vector

#generate the expression
def Generate(Document):
	List = []
	for Sentence in Document:
		for word in Sentence:
			w = AFX.GetWord(word,'Word')
			if AFX.isWord(w):
				List.append(w)
	return List

#caculate the cosine similarity between gloss and document
def Caculate(Doc1, Doc2):

	#Genetate two document into list, and Add
	List1 = Generate(Doc1)
	List2 = Generate(Doc2)
	L = set(List1+List2)

	#get the term frequency of two documents
	TfDoc1 = TermFrequency(List1,L)
	TfDoc2 = TermFrequency(List2,L)

	#caculate the cosine similarity
	fractions = 0.0
	numerator = 0.0
	numeA = 0.0
	numeB = 0.0
	for w in L:
		fractions += TfDoc1[w] * TfDoc2[w]
		numeA += math.pow(TfDoc1[w],2)
		numeB += math.pow(TfDoc2[w],2)

	numerator = math.sqrt(numeA) * math.sqrt(numeB)

	return fractions/numerator

#caculate cosine similarity
# def Cosine_Similarity(w1,w2):
# 	VectorA = {}
# 	VectorB = {}

# 	DicA = tf(w1)
# 	DicB = tf(w2)

# 	mlist = set(w1 + w2)
# 	VectorA = init_vector(DicA,mlist)
# 	VectorB = init_vector(DicB,mlist)

# 	fractions = 0.0
# 	numerator = 0.0
# 	numeA = 0.0
# 	numeB = 0.0
# 	for w in mlist:
# 		fractions += VectorA[w] * VectorB[w]
# 		numeA += math.pow(VectorA[w],2)
# 		numeB += math.pow(VectorB[w],2)

# 	numerator = math.sqrt(numeA) * math.sqrt(numeB)

# 	return fractions/numerator

#create vector for the documents
# def init_vector(WordSet,mlist):
# 	Vector = {}
# 	for w in mlist:
# 		c = WordSet.get(w,0)
# 		Vector[w] = c

# 	return Vector




