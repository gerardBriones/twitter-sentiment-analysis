Project: Semeval 2016 Task 4 - Twitter Sentiment Analysis
Authors: Gerard Briones
Date: 10/1/2015

Description:
	With the emergence of new forms of electronic communications has come the difficulty to automate the process
of mining and understanding the content of these new methods of communication. Tweets, in particular, are extremely
popular and has recently proven to be a challenege. Tweets are messages that are limited to 140 characters and the
language used is often informal, with creative spelling and punctuation, misspellings, grammatical errors, slang,
new words, URLS, and genre-specific terminology and abbreviations. As a group, we've been tasked with developing
tools and methodologies to better process through this information in order to obtain the sentiment behind the given
messages. This subtask, A, focuses on classifying the sentiment of a tweet as either positive, negative, or neutral.

Outline:
	0) load data using dataLoader.py
		- reads in train_A_output.tsv
		- separates data into a training set and a testing set (train_data_taskA.tsv and test_data_taskA.tsv)
	1) read in each line from input
		- each line is structured as: tweet_id1, tweet_id2, start_token, end_token, predictive_class, message
	2) enter the tweet id into a hash in order to keep track of duplicates
	3) remove special characters from the message
	4) remove stop words from the message
	5) extract ngrams from the message
		- an ngram is a contiguous sequence of N words from a given text
	6) create a large hash to track the frequency of the ngrams
	7) create a smaller hash to track the frequency of the ngrams for the given tweet
	8) after each tweet has been processed, create a feature vector from the ngrams 
		above a given frequency threshold
		- a feature vector is a data model which we used to structure our data.
		- each row signifies a tweet
		- each column signifies a word and its frequency
	9) write feature vector to a .arff file for WEKA processing
	10) use WEKA to classify the .arff using 4 classifiers:
		* naive bayes
		* naive bayes multinomial
		* decision tree j48
		* decision tree random forest
Input:
	train_A_output.tsv
	- this is the .tsv obtained by using the 'twitter_download' script written by Alan Ritter for our task.
	- this contains all of the tweet data

Output:
	4 for baseline
	<CLASSIFER TYPE>_bl.txt
	- this is output by WEKA after the classifier has finished running
	- this contains the results of the classifier

	4 for presented method
	<CLASSIFER TYPE>_pm.txt
	- this is output by WEKA after the classifier has finished running
	- this contains the results of the classifier

Work Distribution:
	dataCleaner.py - Written mostly by Kasun, Gerard aided in some debugging and feature writing.
	dataLoader.py - Written equally by Kasun and Gerard. Gerard wrote a test python script (preprocessor.py)
					that was partly refactored into the dataLoader.py by Kasun.
	featureVectorCreator_BL.py - Written equally by Kasun and Gerard. Again, Gerard had previous work in initial
								processing in preprocessor.py, Kasun refactored the code into featureVectorCreator_BL.py.
	featureVectorCreator_BL.py - Written equally by Kasun and Gerard. Again, Gerard had previous work in initial
								processing in preprocessor.py, Kasun refactored the code into featureVectorCreator_PM.py.
								Kasun and Gerard changed the code to handle ngrams instead of solely just unigrams.
	runit.sh - Quick bash script thrown together by Gerard.
	README.txt - Quick readme thrown together by Gerard.
	BASELINES.txt - Written by Gerard.