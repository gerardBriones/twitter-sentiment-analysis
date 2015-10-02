# preprocessor.py
# Authors: Gerard Briones
# Package Dependencies: none

import csv
import os
import dataCleaner

# training data directory
training_data_path = 'train_data/'

# dict for tweet ids
tweet_ids_to_index = {}

# reversed!
index_to_tweet_ids = {}

# dict of unigram hashes for each tweet id
tweet_unigrams = {}

# dict for unigrams
unigrams_to_index = {}

# also reversed!
index_to_unigrams = {}

# 2D list mapping tweet_id to list of words
# 
# tweet_ids 	|	word1	|	word2	|	... 	|	wordN
# tweet_1		|	1		|	0		|			|	2
# tweet_2		|	0		|	3		|			|	1
# tweet_3		|	2		|	4		|			|	1
list_of_tweets = []

# for each file (tsv) in the training data directory...
for filename in os.listdir(training_data_path):

	# FIRST ROUND OF PROCESSING
	# populate tweet_ids_to_index{} and unigrams_to_index{} with key value pairs
	# tweet_ids_to_index{}:
	# 	key = tweet_id
	# 	value = index
	#
	# unigrams_to_index{}:
	# 	key = word
	# 	value = index
	#
	# these are designed to map tweet_ids and words to an
	# easily accessible index

	# open the input file
	with open(training_data_path + filename, 'rb') as tsv_in:

		# create csv reader for the input file
		tsv_in = csv.reader(tsv_in, delimiter='\t')

		# counter of tweets and words in order to assign and track indices
		tweetCounter = 0
		wordCounter = 0

		# ROW PATTERN - One tweet per line
		#	0	1	  2				3			4			 5
		# id1 | id2 | start_token | end_token | pred_class | text
		
		# for each tweet in file...
		for row in tsv_in:

			# if tweet is not available...
			if row[5] == 'Not Available':
				pass # do nothing!

			else:
				tweet_id = str(row[0])

				# lowercasify, remove special characters, and remove stop words
				# dataCleaner -- removeSpecialCharacters()
				#		removes special characters
				# dataCleaner -- removeStopWords() 
				#		removes stop words
				tokens = dataCleaner.removeStopWords(dataCleaner.removeSpecialCharacters(row[5].lower()), 2)

				# first occurance of tweet id, to prevent tracking duplicates
				if not tweet_id in tweet_ids_to_index:

					# add tweet_id to tweet_ids{} with a value of its associated index
					tweet_ids_to_index[tweet_id] = tweetCounter
					tweetCounter += 1

					# for each word in tweet...
					for token in tokens:

						# first occurance of word, to prevent tracking duplicates
						if not token in unigrams_to_index:

							# add word to unigrams_to_index{} with a value of its associated index
							unigrams_to_index[token] = wordCounter
							wordCounter += 1

	# REVERSE THE DICTS!
	for tweet_id in tweet_ids_to_index:
		index_to_tweet_ids[tweet_ids_to_index[tweet_id]] = tweet_id
	for word in unigrams_to_index:
		index_to_unigrams[unigrams_to_index[word]] = word

	# SECOND ROUND OF PROCESSING
	# populate list_of_tweets[] with tweet_ids and messages
	# [] first index = tweet_ids[tweet_id]
	# value = index
	#
	# this is built this way in order to easily track unique tweet_ids
	# and words in order to properly build the 2D array

	# reopen the input file
	with open(training_data_path + filename, 'rb') as tsv_in2:

		# create csv reader for the input file
		tsv_in2 = csv.reader(tsv_in2, delimiter='\t')

		# initialize first dimension of list_of_tweets for tweet_ids
		list_of_tweets = [0] * (len(tweet_ids_to_index))

		# initialize second dimension of list_of_tweets for bag of words
		for i in range(0, len(tweet_ids_to_index)):
			list_of_tweets[i] = [0] * (len(unigrams_to_index))

		# temporary dict to keep track of tweet_ids
		temp_tweet_ids = {}

		# ROW PATTERN - One tweet per line
		#	0	1	  2				3			4			 5
		# id1 | id2 | start_token | end_token | pred_class | text
		
		# for each tweet in file...
		for row in tsv_in2:
			
			# if tweet is not available...
			if row[5] == 'Not Available':
				pass # do nothing!

			else:
				tweet_id = str(row[0])

				# lowercasify, remove special characters, and remove stop words
				# dataCleaner -- removeSpecialCharacters()
				#		removes special characters
				# dataCleaner -- removeStopWords() 
				#		removes stop words
				tokens = dataCleaner.removeStopWords(dataCleaner.removeSpecialCharacters(row[5].lower()), 2)

				# only tracking unique tweet_ids
				if not tweet_id in temp_tweet_ids:

					# mark tweet as seen
					temp_tweet_ids[tweet_id] = 1

					# build bag of words for each unique tweet
					for token in tokens:
						list_of_tweets[tweet_ids_to_index[tweet_id]][unigrams_to_index[token]] += 1

for unigram in unigrams_to_index:
	print unigram, ' : ', unigrams_to_index[unigram]