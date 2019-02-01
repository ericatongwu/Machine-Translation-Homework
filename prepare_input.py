# This file will prepare the sentences.txt by
# removing punctuations 

import re
import sys

# remove desired punctuations in a sentence
# input: str
# output: str
def remove_punctuations(s):
	punctuations = r"[^\w\s]"
	return re.sub(punctuations, '', s)

# read the file
# input: str (the file name)
# output: list, the content of the text file
def read_file(file_name):
	with open(file_name) as f:
		data = f.readlines()
		data = [remove_punctuations(x) for x in data]
	return data

# main function
def main():
	# open file
	data = read_file('sentences.txt')

	for sentence in data:
		sys.stdout.write(sentence)
		sys.stdout.flush()

if __name__ == '__main__':
	main()