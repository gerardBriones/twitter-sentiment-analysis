Project: Semeval 2016 Task 4 - Twitter Sentiment Analysis
Authors: Gerard Briones (Gerard wrote this readme, not the entire project)
Date: 10/1/2015

-- Note : Syed could not participate in stage 1 due to travel --

Description:
	With the emergence of new forms of electronic communications has come the difficulty to automate the process
of mining and understanding the content of these new methods of communication. Tweets, in particular, are extremely
popular and has recently proven to be a challenege. Tweets are messages that are limited to 140 characters and the
language used is often informal, with creative spelling and punctuation, misspellings, grammatical errors, slang,
new words, URLS, and genre-specific terminology and abbreviations. As a group, we've been tasked with developing
tools and methodologies to better process through this information in order to obtain the sentiment behind the given
messages. This subtask, A, focuses on classifying the sentiment of a tweet as either positive, negative, or neutral.

Outline: (this process is repeated over each method of analysis, i.e. unigrams, bigrams, combined)
	0) load data using dataLoader.py
		- reads in train_A_output.tsv
		- separates data into a training set and a testing set (train_data_taskA.tsv and test_data_taskA.tsv)
	1) data is cleaned using dataCleaner.py
	2) read in each line from input
		- each line is structured as: tweet_id1, tweet_id2, start_token, end_token, predictive_class, message
	3) enter the tweet id into a hash in order to keep track of duplicates
	4) remove special characters from the message
	5) remove stop words from the message
	6) extract ngrams from the message
		- an ngram is a contiguous sequence of N words from a given text
	7) create a large hash to track the frequency of the ngrams
	8) create a smaller hash to track the frequency of the ngrams for the given tweet
	9) after each tweet has been processed, create a feature vector from the ngrams 
		above a given frequency threshold
		- a feature vector is a data model which we used to structure our data.
		- each row signifies a tweet
		- each column signifies a word and its frequency
	10) write feature vector to a .arff file for WEKA processing
	11) use WEKA to classify the .arff using 4 classifiers:
		* naive bayes
		* naive bayes multinomial
		* decision tree j48
		* decision tree random forest

Input:
	train_A_output.tsv -- located in data_all directory
	- this is the .tsv obtained by using the 'twitter_download' script written by Alan Ritter for our task.
	- this contains all of the tweet data

Output:
	All output will be deposited in the output directory

	4 for baseline
	<CLASSIFER TYPE>_bl.txt
	- this is output by WEKA after the classifier has finished running
	- this contains the results of the classifier

	4 for presented method
	<CLASSIFER TYPE>_pm.txt
	- this is output by WEKA after the classifier has finished running
	- this contains the results of the classifier

	4 for combined method
	<CLASSIFER TYPE>_combined.txt
	- this is output by WEKA after the classifier has finished running
	- this contains the results of the classifier

Work Distribution:
	-- note : check in source code to find individualized comments and authorship tagging
	-- note : Gerard's work focused mainly on general script writing and feature vector creating
				Kasun focused on WEKA integration. Both worked with one another in creation of
				this entire project, down to each script. Pair programming and constant communication
				when individually coding was used in order to aid development.

	dataCleaner.py - Written mostly by Kasun, Gerard aided in some debugging and feature writing.
	dataLoader.py - Written equally by Kasun and Gerard. Gerard wrote a test python script (preprocessor.py)
					that was partly refactored into the dataLoader.py by Kasun.
	featureVectorCreator_BL.py - Written equally by Kasun and Gerard. Again, Gerard had previous work in initial
								processing in preprocessor.py, Kasun refactored the code into featureVectorCreator_BL.py.
	featureVectorCreator_BL.py - Written equally by Kasun and Gerard. Again, Gerard had previous work in initial
								processing in preprocessor.py, Kasun refactored the code into featureVectorCreator_PM.py.
								Kasun and Gerard changed the code to handle ngrams instead of solely just unigrams.
	featureVectorCreator_Combined.py - Written equally by Kasun and Gerard. Again, previous work was used in initial
								processing that was written by Gerard. Kasun reworked the code to create a combined
								ngram feature vector using previously used methods.
	runit.sh - Quick bash script thrown together by Gerard.
	README.txt - Quick readme thrown together by Gerard.
	BASELINES.txt - Written by Gerard.