import random

def process_file(filename):
	dict = {}
	f = open(filename)
	read_file = f.read()
	f.close()
	word_list = read_file.split()
	while len(word_list) >= 3:
		prefix = (word_list[0], word_list[1])
		if prefix in dict.keys():
			dict[prefix].append(word_list[2])
		else:
			dict[prefix] = [word_list[2]]
		prefix = shift(prefix, word_list[2])
		word_list = word_list[1:]
	return dict

def shift(tuple_pair, second_argument):
	#remove first element
	fe_removed = tuple_pair[1:]
	#add second argument to the end
	new_tuple = fe_removed + (second_argument,)
	return new_tuple

def build_sentence(mapping):
	punct_found = False
	sentence_words = []
	space = ' '
	punct = ['.', '?', '!']
	if len(mapping) != 0:
		key_list = mapping.keys()
		working_key = random.choice(key_list)
		sentence_words.append(working_key[0])
		sentence_words.append(working_key[1])
		while (punct_found == False) and (working_key in key_list):
			if sentence_words[-1][-1] not in punct:
				element = random.choice(mapping[working_key])
				sentence_words.append(element)
				working_key = shift(working_key, element)
			else:
				punct_found = True
		sentence = space.join(sentence_words)
		sentence = sentence.capitalize()
		return sentence

def build_paragraph(dict, times):
	paragraph_list = []
	space = ' '
	for num in range(times-1):
		sentence = build_sentence(dict)
		paragraph_list.append(sentence)
	paragraph = space.join(paragraph_list)
	return paragraph

def main():
	print build_paragraph((process_file('sample5.txt')), 5)
	#print process_file('sample5.txt')


if __name__ == "__main__":
	main()