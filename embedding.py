""" This file would build embedding for this translation system.
	By using the index of each sentence to code each word and 
	reverse them to get corresponding output.
"""

import nltk
from gensim.models import Word2Vec

# read txt file into sentences
def read_file(file_name):
	with open(file_name) as f:
		sentences = f.readlines()
	return sentences

# tokenize each setence, use index to generate a new list corresponding 
# to original sentence.
def word2index(sentences):
	
	corr_list = []
	for line in sentences:
		token_line = nltk.word_tokenize(line)
		index_line = []
		for i in range(0, len(token_line)):
			index_line.append(str(i))
		corr_list.append(index_line)
	return corr_list
sample = []
# creating the model
def model(corr_list):
	model = Word2Vec(corr_list, size=50, min_count=1, window=5, workers=4, sg=1)
	model.save("embedding.bin")
	model = Word2Vec.load("embedding.bin")

	for element in corr_list:
		sentence = []
		for index_id in element:
			new_id = model.wv[index_id]
			sentence.append(new_id)
		sample.append(sentence)

	return sample


# main function
def main():
	
	sentences = read_file('input.txt')
	corr_list =  word2index(sentences)
	print model(corr_list)
if __name__ == '__main__':
	main()
# sentences = []
# with open("input.txt") as f:
# 	for sentence in f:
# 		tokens = nltk.word_tokenize(sentence)
# 		sentences.append(tokens)

# print sentences

