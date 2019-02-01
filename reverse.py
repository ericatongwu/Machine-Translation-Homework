# generating a target file for training
# this file contains the reverse of the source sentences

import re

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
		content = f.readlines()
		content = [remove_punctuations(x) for x in content]

	return content


# reverse each element of content into the target sentence
# input: list of strings
# output: list of reversed input
def reverse(content):
	reverse_content = []
	for element in content:
		list_element = element.split()
		reverse = list_element[::-1]
		element = " ".join(reverse)
		reverse_content.append(element)

	return reverse_content

# main function
def main():
	# open file
	content = read_file('sentences.txt')

	for sentence in reverse(content):
		print sentence


if __name__ == '__main__':
	main()

	

	
