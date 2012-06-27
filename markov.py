import random
import tweepy

def process_file(filename):
	dict = {}
	f = open(filename)
	read_file = f.read()
	f.close()
	word_list = read_file.split()

	for i in range(len(word_list)-2):
		prefix = (word_list[i], word_list[i+1])
		suffix = word_list[i+2]
		if dict.get(prefix) is not None:
			dict[prefix].append(suffix)
		else:
			dict[prefix] = [suffix]

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
		sentence_words[0] = sentence_words[0].capitalize()
		sentence = " ".join(sentence_words)
		return sentence

def build_paragraph(dict, times):
	paragraph_list = []
	space = ' '
	for num in range(times):
		sentence = build_sentence(dict)
		paragraph_list.append(sentence)
	paragraph = space.join(paragraph_list)
	return paragraph

def build_tweet(source, n):
	check = True
	while check:
		if len(build_paragraph((process_file(source)), n)) <= 140:
			print build_paragraph((process_file(source)), n)
			print n
			print len(build_paragraph((process_file(source)), n))
			check = False
		else:
			n = n-1



def main():
	build_tweet('emma.txt', 5)


if __name__ == "__main__":
	main()