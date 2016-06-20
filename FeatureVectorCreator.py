import csv
import os
import re
import sys

tweets = {}
sentiments = {}
bag_of_ngrams = {}
selected_ngrams = {}

def load_data(input_file_path, n):
	with open(input_file_path, 'r') as input_file:
		file_reader = csv.reader(input_file, delimiter = '\t')
		temp_ngram_list = []
		for row in file_reader:
			tweet_id = row[0]
			tweet = row[1]
			sentiment = row[2]

			if(tweet_id not in sentiments):
				sentiments[tweet_id] = sentiment
				tweets[tweet_id] = ngramify(tweet, n)
				
def ngramify(tweet, n):
	atoms = tweet.split(' ')
	ngrams = []
	for i in range(0, len(atoms)):
		if(i + n > len(atoms)):
			break

		ngram = str.join(' ', atoms[i:(i + n)])
		ngrams.append(ngram)

		if(ngram not in bag_of_ngrams):
			bag_of_ngrams[ngram] = 0
		bag_of_ngrams[ngram] += 1

	return ngrams

def select_frequent_ngrams(threshold):
	for ngram in bag_of_ngrams:
		count = bag_of_ngrams[ngram]
		if(count >= threshold):
			selected_ngrams[ngram] = count

def create_feature_vector():
	feature_vector = {}

	for tweet_id in sentiments:
		print(tweet_id)
		feature_vector[tweet_id] = selected_ngrams
		feature_vector[tweet_id] = {k: 0 for (k, v) in selected_ngrams.items()}
		for ngram in tweets[tweet_id]:
			if(ngram in selected_ngrams):
				feature_vector[tweet_id][ngram] += 1

	# with open(input_file_path, 'r') as input_file:
	# 	file_reader = csv.reader(input_file, delimiter = '\t')
	# 	for row in file_reader:
	# 		tweet_id = row[0]
	# 		tweet = row[1]
	# 		sentiment = row[2]


	# 		for i in range(0, len(tweet)):
	# 			if(i + n > len(tweet)):
	# 				break

	# 			ngram = str.join(' ', tweet[i:(i + n)])

	# 			if(ngram in selected_ngrams):
	# 				feature_vector[tweet_id][ngram] += 1

	return feature_vector