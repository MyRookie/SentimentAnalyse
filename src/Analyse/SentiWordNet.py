import sys
import AFX

#split the sentence by '\t'
def split_line(line):
	col = line.split("\t")
	return col

def get_words(col):
    words_ids = col[4].split(" ")
    words = {}
    for w in words_ids:
    	notation = w.split("#")[1]
    	if len(w.split("#")[1]) <= 1:
	    	notation = '0' + notation
    	words[w.split("#")[0]] = notation
    return words

def get_positive(col):
	return col[2]

def get_negative(col):
	return col[3]

def get_objective(col):
	return (float(col[2]) - float(col[3]))

def get_gloss(col):
	return col[5]

def return_all_gloss(filePath, word, pos):
	gloss = {}
	f = open(filePath)
	for line in f:
		if not line.startswith("#"):
			cols = split_line(line)
			words = get_words(cols)

			if words.has_key(word):
				if AFX.GetWordNetPoS(word,words[word],pos) is True:
					gloss[get_gloss(cols)] = get_objective(cols)

	return gloss

def get_score(filePath, word):

	f = open(filePath)
	for line in f:
		if not line.startswith("#"):
			cols = split_line(line)
			words = get_words(cols)


			if word in words:
				print(get_gloss(cols))

if __name__ == "__main__":

	path = "../Library/SentiWordNet_3.0.txt"
	word = input("input word here: ")

	get_score(path, word)

