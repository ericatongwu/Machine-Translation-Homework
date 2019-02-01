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
		corr_list.append(index_line[::-1])
	return corr_list



# main function
def main():
	
	sentences = read_file('target.txt')
	outs =  word2index(sentences)
	print outs
if __name__ == '__main__':
	main()