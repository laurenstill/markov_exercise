import random
import tweepy
import sys

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
		message = build_paragraph((process_file(source)), n)
		check = False
		return message

def tweet_authentication(message_tweet):
	CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXX'
	CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXX'
	ACCESS_KEY = 'XXXXXXXXXXXXXXXXXX'
	ACCESS_SECRET = 'XXXXXXXXXXXXXXXXXX'

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	api.update_status(message_tweet)

def check_for_140(tweet_message):
	size_check = False
	while size_check == False:
		if len(tweet_message) > 140:
			tweet_message = build_tweet('zed_text.txt', 1)
		else:
			size_check = True
			return tweet_message

def post_tweet(tweet_message):
	tweet_authentication(tweet_message)
	print "Posted on Twitter!"

def command_list():
	print "#" * 70
	print "        Wonderful ShawZed Twitter Bot, for Best Tweets"
	print "\t Commands:"
	print "\t \t >>> 'y' = yes, post"
	print "\t \t >>> 'n' = no, do not post"
	print "\t \t >>> 'y,<twitter_user>' = yes, post @<twitter_user>"
	print "\t \t >>> 'q' = quit the amazing ShawZed Twitter Creator"
	print "#" * 70
	print "\n"

def should_we_post():
	quit = False
	while quit == False:
		message = build_tweet('zed_text.txt', 1)
		should_we_message = check_for_140(message)
		print "Generated tweet: %s" %should_we_message
		should_we = raw_input("Should we post it?:  ")
		if should_we[0] == "y":
			if len(should_we) > 2:
				command_string = should_we.split(',')
				#returns [y, name]
				tweet_name = command_string[1]
				#returns tweet username
				directed_twitter = "@" + tweet_name + " " + should_we_message
				post_tweet(directed_twitter)
			else: 
				post_tweet(should_we_message)
		elif should_we == 'n':
			print "Tweet was not posted."
		elif should_we == 'q':
			quit = True
		else:
			print "What, that isn't a y or a n."

def main():
	command_list()
	should_we_post()



if __name__ == "__main__":
	main()