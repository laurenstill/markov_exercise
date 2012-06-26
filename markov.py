import random

"""
markov.py

Reference text: section 13.8, how to think like a computer scientist

Do markov analysis of a text and produce mimic text based off the original.

Markov analysis consists of taking a text, and producing a mapping of prefixes to suffixes. A prefix consists of one or more words, and the next word to follow the prefix in the text. Note, a prefix can have more than one suffix.

Eg: markov analysis with a prefix length of '1'

    Original text:
        "The quick brown fox jumped over the lazy dog"

        "the": ["quick", "lazy"]
        "quick": ["brown"]
        "brown": ["fox"]
        "fox": ["jumped"]
        ... etc.

With this, you can reassemble a random text similar to the original style by choosing a random prefix and one of its suffixes, then using that suffix as a prefix and repeating the process.

You will write a program that performs markov analysis on a text file, then produce random text from the analysis. The length of the markov prefixes will be adjustable, as will the length of the output produced.
""" 

def process_file(filename):
	dict = {}

	# create a list of lines from the file
	collection_of_lines = []
	f = open(filename)
	for line in filename:
		line_string = f.readline()
		collection_of_lines.append(line_string)
	f.close()

	# look at each line, and split
	for line in collection_of_lines:
		word_list = line.split()
		print word_list
		if len(word_list) >= 3:
			prefix = (word_list[0], word_list[1])
			dict[prefix] = [word_list[2]]
			print dict
			shift(prefix, word_list[2])
			print dict
	return dict

def shift(tuple_pair, second_argument):
	#remove first element
	fe_removed = tuple_pair[1:]
	#add second argument to the end
	new_tuple = fe_removed + (second_argument,)
	return new_tuple

def build_sentence(mapping):
	#use random.choice(seq)
	space = ' '
	if len(mapping) != 0:
		for key in mapping:
			element = random.choice(mapping[key])
			word1 = key[0]
			word2 = key[1]
			string = word1 + space + word2 + space + element
		return string


def main():
	mapping = process_file('sample2.txt')
	sentence = build_sentence(mapping)
	print sentence
	return sentence


if __name__ == "__main__":
	main()