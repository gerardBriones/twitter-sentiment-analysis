# featureVectorCreator_BL.py
# Authors: Gerard Briones, Kasun Amarasinghe
# creates the featurevector for the baseline and saves to a .arff file

import csv
import os
import dataCleaner

# training data directory
training_data_path = 'train_data/'

# testing data directory
testing_data_path = 'test_data/'

# Arff file directory
arff_file_path = 'arff_data/'

#train data file name
train_file = 'train_data_taskA.tsv'

#test data file name
test_file = 'test_data_taskA.tsv'

# Arff for training
arff_train_file = 'arff_train_bl.arff'

# Arff for testing
arff_test_file = 'arff_test_bl.arff'

# all words and frequencies in the training directory
unigrams_train = {}

# all words and frequencies in the testing directory
# not used to create FV, for book keeping purposes
unigrams_test = {}

# holds words with a pre defined frequency 
selected_unigrams_train = {}

# holds words with a pre defined frequency 
# not used to create FV, for book keeping purposes
selected_unigrams_test = {}

# all tweet ids in the training set, stores the sentiment class as the value
tweet_ids_train = {}

# all tweet ids in the testing set, stores the sentiment class as the value
tweet_ids_test = {}

# predefined freq threshold
# the minimum frequency a word should appear in the tweet to be selected
freq_thresh = 1

# dicts to hold the sentiment classes that exist and number of elements in each class (training and testing)
# Assumption - Objective tweets are neutral ( 3 - class classification task)
#sentiment_classes_train = {'objective':0,'positive':0, 'neutral':0, 'negative':0}
#sentiment_classes_test = {'objective':0,'positive':0, 'neutral':0, 'negative':0}

# 2nd attempt - remove objective tweets from dataset
sentiment_classes_train = {'positive':0, 'neutral':0, 'negative':0} 
sentiment_classes_test = {'positive':0, 'neutral':0, 'negative':0}

# The training and testing TDM/ FV
# TDM - Term Document Matrix, FV - Feature Vector
tdm_train = {}
tdm_test = {}

# datareader (input_file, unigrams_dictionary,  tweetIDs_dictionary, SentimentClass_dictionary
# populating the unigrams dictionary
# collects all the unique words that exist in the training set
# these words are considered as the keywords in the feature vector
def dataReader(in_file_path, n_grams, tid_dict, sc_dict):
	with open(in_file_path, 'rb') as tsv_in:
		#create csv reader for the input file
		tsv_in = csv.reader(tsv_in, delimiter='\t')

		# File format
		# TweetID | Tweet | class (sentiment)
		for row in tsv_in:
			#print row
			tid = row[0]
			tweet = row[1]
			if len(row)>2:
				sentiment = row[2]
				# only consider unique tweets
				if not tid in tid_dict:
					if sentiment in sc_dict:
						tid_dict[tid] = sentiment
						sc_dict[sentiment] += 1
						# obtaining individual words from the tweet
						# Special characters, numbers are removed and converted to lower case
						words = dataCleaner.removeStopWords(dataCleaner.removeSpecialCharacters(tweet),1)
						for token in words:
							if token in n_grams:
								n_grams[token] +=1
							else:
								n_grams[token] = 1

# Extracts the words with higher frequency than the threshold
# Reduces the sparseness of the matrix
def chooseFrequentWords (n_grams, selected_n_grams, freq):
	# removing words which appear less than the frequency	
	#selected_n_grams = {x:v for (x,v)  in n_grams.items() if v > freq}
	
	for word in n_grams:
		#print n_grams[word]
		value = n_grams[word]
		if value > freq:
			selected_n_grams[word] = value


# creates the feature vector from the extracted data
def createFV(in_file_path, selected_n_grams, tdm_dict, tid_dict, sc_dict):
	with open(in_file_path, 'rb') as tsv_in:
		# Initializing the TDM (list of dictionaries)
		for tid in tid_dict:
			tdm_dict[tid] = selected_n_grams
			tdm_dict[tid] = {x:0 for (x,v)  in tdm_dict[tid].items()}
		
		#create csv reader for the input file
		tsv_in = csv.reader(tsv_in, delimiter='\t')
		for row in tsv_in:
			tid = row[0]
			tweet = row[1]
			if len(row)>2:
				words = dataCleaner.removeStopWords(dataCleaner.removeSpecialCharacters(tweet), 1)
				if tid in tid_dict:
					for token in selected_n_grams:
						if token in words:
							tdm_dict[tid][token]+=1


# writes the created feature vector to a file
def writeFVtoARFF(out_file_path, selected_n_grams, tdm_dict, tid_dict, sc_dict, header):
	# creating the Training ARFF file
	fp = open(out_file_path, 'w')
	fp.write("@RELATION\t"+header+"\n")

	counter = 1
	for words in selected_n_grams.keys():
		fp.write("@ATTRIBUTE\t"+str(counter)+"_"+str(words)+"\tREAL\n")
		counter +=1
	
	fp.write("@ATTRIBUTE\tclass\t{")

	counter = 0
	for st in sc_dict:
		if(counter<len(sc_dict.keys())-1):
		# Objective tweets are considered as neutral 		
			if st != 'objective':
				fp.write(st)
				fp.write(',')
		else:
			fp.write(st)
		counter+=1
	fp.write('}\n')
	fp.write("\n")
	fp.write("@DATA\n")

	for tid in tid_dict:
		for token in selected_n_grams:
			fp.write(str(tdm_dict[tid][token])+",")

		# Objective tweets are considered as Neutral
		if tid_dict[tid] == 'objective':
			tid_dict[tid] = 'neutral'
		fp.write(tid_dict[tid])
		fp.write("\n")
	
	fp.close()


#--------------- Training data----------------------------------

# Reading the training dataset
dataReader(training_data_path + train_file, unigrams_train, tweet_ids_train, sentiment_classes_train)


# Extracting words above frequency threshold 
chooseFrequentWords(unigrams_train, selected_unigrams_train, freq_thresh)

# Creating the FV/TDM
createFV(training_data_path + train_file, selected_unigrams_train, tdm_train, tweet_ids_train,  sentiment_classes_train)

# Writing FV/TDM to file
writeFVtoARFF(arff_file_path+arff_train_file, selected_unigrams_train, tdm_train, tweet_ids_train, sentiment_classes_train, 'Sentiment_Analysis_Training_Baseline')


#--------------- Testing data----------------------------------

# Reading the training dataset
dataReader(testing_data_path + test_file, unigrams_test, tweet_ids_test, sentiment_classes_test)


# Extracting words above frequency threshold - Not necessary for test set 
#chooseFrequentWords(unigrams_test, selected_unigrams_test, freq_thresh)


# Creating the FV/TDM
createFV(testing_data_path + test_file, selected_unigrams_train, tdm_test, tweet_ids_test,  sentiment_classes_test)

# Writing FV/TDM to file
writeFVtoARFF(arff_file_path+arff_test_file, selected_unigrams_train, tdm_test, tweet_ids_test, sentiment_classes_test, 'Sentiment_Analysis_Testing_Baseline')



