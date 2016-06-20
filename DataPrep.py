#!/usr/bin/python3.5

import csv
import os
import re
import sys

stopwords = []

def remove_special_characters(s):
	return re.sub('[^A-Za-z ]+', '', s)

def remove_stopwords(s):
	if not stopwords:
		stopword_file = 'stopword_list.txt'
		stopword_list = open('supporting_data/' + stopword_file)
		for stopword in stopword_list:
			stopword = remove_special_characters(stopword)
			stopwords.append(stopword)

	str_decomposed = s.split()
	key_words = []
	for word in str_decomposed:
		if word not in stopwords:
			key_words.append(word)

	return str.join(' ', key_words)

def convert_emoticons(s):

	# matches variations of :) -- smileEmoticon
	s = re.sub('\b[:=8]-?[)\]}]|[([{]-?[:=8]\b', 'smileEmoticon', s)

	# matches variations of :( -- frownEmoticon
	s = re.sub('\b[:=8]-?[([{]|[)\]}]-?[:=8]\b', 'frownEmoticon', s)

	# matches variations of ;) -- winkEmoticon
	s = re.sub('\b;-?[)\]}]|[([{]-?;\b', 'winkEmoticon', s)

	# matches variations of :P
	s = re.sub('\b[:=;8]-?[pP]|[dpP]-?[:=;8]\b', 'tongueEmoticon', s)

	# matches variations of :/
	s = re.sub('\b[:=;8]-?[/|\\\]|[/|\\\]-?[:=;8]\b', 'concernEmoticon', s)

	# matches variations of :D
	s = re.sub('\b[:=xX8]-?D\b', 'grinEmoticon', s)
	
	# matches variations of D:
	s = re.sub('\bD-?[:=xX8]\b', 'mirrorGrinEmoticon', s)

	# matches variations of ;D
	s = re.sub('\b;-?D\b', 'winkGrinEmoticon', s)

	# matches variations of :O
	s = re.sub('\b[:=]-?[oO]|[oO]-?[:=]\b', 'surpriseEmoticon', s)

	# matches variations of :')
	s = re.sub('\b[:=][\'`]-?[)\]}]|[([{]-?[\'`][:=]\b', 'tearSmileEmoticon', s)

	# matches variations of :'(
	s = re.sub('\b[:=][\'`]-?[({[]|[)\]}]-?[\'`][:=]\b', 'tearFrownEmoticon', s)

	return s

def load_data(input_file_path, output_file_path, type, mods):
	output_file = open(output_file_path, 'w')
	with open(input_file_path, 'r') as input_file:
		tweet_ids = {}
		file_reader = csv.reader(input_file, delimiter = '\t')
		for row in file_reader:
			tweet_id = row[0]
			if(tweet_id not in tweet_ids):
				tweet_ids[tweet_id] = 1
				sentiment = ''
				tweet = ''
				topic = ''

				if(type.lower() == 'a'):
					sentiment = row[1]
					tweet = row[2]
				elif(type.lower() == 'b'):
					topic = row[1]
					sentiment = row[2]
					tweet = row[3]

				if(tweet.lower() == 'not available'):
					print(tweet)
					pass

				if('emoticons' in mods):
					tweet = convert_emoticons(tweet)
				tweet = remove_special_characters(tweet)
				tweet = remove_stopwords(tweet)

				output_file.write(str(tweet_id) + '\t' + tweet + '\t' + sentiment + '\t' + topic + '\n')

# print(remove_stopwords('i can\'t feel my face when i\'m with you'))
load_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:])
# print(sys.argv[4:])