# preprocessor.py
# Authors: Gerard Briones, Kasun Amarasinghe
# Package Dependencies: none

import csv
import os
import dataCleaner

# training data directory
training_data_path = 'train_data/'

# dict for tweet ids
tweet_ids = {}

# dict of unigram hashes for each tweet id
tweet_unigrams = {}

# dict for unigrams
unigrams = {}

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
	# populate tweet_ids{} and unigrams{} with key value pairs
	# tweet_ids{}:
	# 	key = tweet_id
	# 	value = index
	#
	# unigrams{}:
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
				tokens = dataCleaner.removeStopWords(dataCleaner.removeSpecialCharacters(row[5].lower()))

				# first occurance of tweet id, to prevent tracking duplicates
				if not tweet_id in tweet_ids:

					# add tweet_id to tweet_ids{} with a value of its associated index
					tweet_ids[tweet_id] = tweetCounter
					tweetCounter += 1

					# for each word in tweet...
					for token in tokens:

						# first occurance of word, to prevent tracking duplicates
						if not token in unigrams:

							# add word to unigrams{} with a value of its associated index
							unigrams[token] = wordCounter
							wordCounter += 1

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
		list_of_tweets = [0] * (len(tweet_ids))

		# initialize second dimension of list_of_tweets for bag of words
		for i in range(0, len(tweet_ids)):
			list_of_tweets[i] = [0] * (len(unigrams))

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
				tokens = dataCleaner.removeStopWords(dataCleaner.removeSpecialCharacters(row[5].lower()))

				# only tracking unique tweet_ids
				if not tweet_id in temp_tweet_ids:

					# mark tweet as seen
					temp_tweet_ids[tweet_id] = 1

					# build bag of words for each unique tweet
					for token in tokens:
						list_of_tweets[tweet_ids[tweet_id]][unigrams[token]] += 1

print unigrams