# preprocessor.py
# Authors: Gerard Briones, Kasun Amarasinghe
# Package Dependencies: None

import csv
import os

# training data directory
training_data_path = 'train_data/'

# dict for tweet ids
tweet_ids = {}

# dict for unigrams
unigrams = {}

# for each file (tsv) in the training data directory...
for filename in os.listdir(training_data_path):

	# open the input file
	with open(training_data_path + filename, 'rb') as tsv_in:

		# create csv reader for the input file
		tsv_in = csv.reader(tsv_in, delimiter='\t')

		# ROW PATTERN - One tweet per line
		#	0	1	  2				3			4			 5
		# id1 | id2 | start_token | end_token | pred_class | text
		
		# for each tweet in file...
		for row in tsv_in:
			tweet_id = row[0]
			tokens = row[5].split()

			if not tweet_id in  tweet_ids:

				# add tweet_id to tweet_ids{}
				tweet_ids[tweet_id] = 1

				# for each unigram in tweet...
				for token in tokens:

					# add unigram to unigrams{}
					if not token in unigrams:
						unigrams[token] = 1

					# increment unigram count in unigrams{}	
					else:
						unigrams[token] += 1

			else:
				# increment tweet_id count in tweet_ids{}
				tweet_ids[tweet_id] += 1

# printing unigrams to terminal
for unigram in unigrams:
	print unigram, ' : ', unigrams[unigram]