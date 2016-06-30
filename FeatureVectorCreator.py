import csv
import os
import re
import sys

tweets = {}
tweet_sentiments = {}
sentiment_totals = {}
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

			if(tweet_id not in tweet_sentiments):
				tweet_sentiments[tweet_id] = sentiment
				tweets[tweet_id] = ngramify(tweet, n)

			if(sentiment not in sentiment_totals):
				sentiment_totals[sentiment] = 0
			sentiment_totals[sentiment] += 1
				
def ngramify(tweet, n):
	atoms = tweet.split(' ')
	ngrams = []
	for i in range(0, len(atoms)):
		if(i + n > len(atoms)):
			break

		ngram = str.join('_', atoms[i:(i + n)])
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

	for tweet_id in tweet_sentiments:
		# print(tweet_id)
		feature_vector[tweet_id] = selected_ngrams
		feature_vector[tweet_id] = {k: 0 for (k, v) in selected_ngrams.items()}
		for ngram in tweets[tweet_id]:
			if(ngram in selected_ngrams):
				feature_vector[tweet_id][ngram] += 1

	return feature_vector

def arffify(arff_filename, header, feature_vector):
	arff_file = open(arff_filename, 'w')
	arff_file.write('@RELATION\t' + header + '\n')

	counter = 1
	for ngram in selected_ngrams.keys():
		arff_file.write('@ATTRIBUTE\t' + str(counter) + '_'
			+ ngram + '\tREAL\n')
		counter += 1

	arff_file.write('@ATTRIBUTE\tclass\t{'
		+ str.join(',', sentiment_totals.keys()) + '}\n\n')

	arff_file.write('@DATA\n')
	for tweet_id in tweet_sentiments:
		for ngram in selected_ngrams:
			arff_file.write(str(feature_vector[tweet_id][ngram]) + ',')

		arff_file.write(tweet_sentiments[tweet_id] + '\n')

	arff_file.close()