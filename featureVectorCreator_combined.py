# featureVectorCreator_combined.py
# Authors: Gerard Briones, Kasun Amarasinghe
# creates a combined featurevector for unigrams and bigrams and saves to a .arff file
# can be used to combine any two n-gram models, can be extended to combine more as well 

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
arff_train_file = 'arff_train_Combined.arff'

# Arff for testing
arff_test_file = 'arff_test_Combined.arff'

# Storing all training and testing data
store_train_data = []
store_test_data = []

# all words and frequencies in the training directory
n_grams_train_n1 = {}
n_grams_train_n2 = {}

# holds words with a pre defined frequency 
selected_n_grams_train_n1 = {}
selected_n_grams_train_n2 = {}

# all words and frequencies in the testing directory
# not used to create FV, for book keeping purposes
n_grams_test_n1 = {}
n_grams_test_n2 = {}

# holds words with a pre defined frequency 
# not used to create FV, for book keeping purposes
selected_n_grams_test_n1 = {}
selected_n_grams_test_n2 = {}


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
tdm_train_n1 = {}
tdm_train_n2 = {}
tdm_test_n1 = {}
tdm_test_n2 = {}

# loadDatafromFle : loads data from a file and stores in a list of arrays
# Arguments : Path of file, output data array, dictionary for tweet Ids, dictionary for tweet classes
def loadDataFromFile(in_file_path, storing_array, tid_dict, sc_dict):
	with open(in_file_path, 'rb') as tsv_in:
		#create csv reader for the input file
		tsv_in = csv.reader(tsv_in, delimiter='\t')
		
		# File format
		# TweetID | Tweet | class (sentiment)
		for row in tsv_in:
			tid = row[0]
			# only consider unique tweets
			if not tid in tid_dict:
				if len(row)>2:
					sentiment = row[2]
					# storing the file as a array
					if sentiment in sc_dict:
						storing_array.append(row)
						tid_dict[tid] = sentiment
						sc_dict[sentiment]+=1					
					
# printData: prints stored data
# Arguments: array list with data		
def printData(storing_array):
	for tweet in storing_array:
		print tweet


# ngramReader: populates ngram dictionaries from tweets
# arguments: arraylist containing data, ngrams dictionary, n (1 for unigram, 2 for bigram etc.) 
def ngramReader(data_array, n_grams, num_grams):
	for row in data_array:
		tweet = row[1]
		# cleaning the tweet : subroutine from dataCleaner.py
		words = dataCleaner.removeStopWords(dataCleaner.removeSpecialCharacters(tweet),num_grams)
		for token in words:
			if token in n_grams:
				n_grams[token] +=1
			else:
				n_grams[token] = 1
				
	

# chooseFrequentWords: Rmoves n-grams with lower or equal frequency than/to the threshold
# Arguments: ngrams dictionary, remaining(selected) ngrams dictionary, frequency threshold
def chooseFrequentWords (n_grams, selected_n_grams, freq):
	
	for word in n_grams:
		value = n_grams[word]
		if value > freq:
			selected_n_grams[word] = value

# createFV: creates the feature vector from the extracted data
# arguments: stored data array list, selected ngrams dictionary, dictionary to hold FV/TDM, tweetID dictionary, n
def createFV(data_array, selected_n_grams, tdm_dict, tid_dict, num_grams):
	
	# initializing the tdm dictionary of dictionaries		
	for tid in tid_dict:
		tdm_dict[tid] = selected_n_grams
		tdm_dict[tid] = {x:0 for (x,v)  in tdm_dict[tid].items()}
		
	for row in data_array:
		tid = row[0]
		tweet = row[1]
		
		# cleaning the tweet : subroutine from dataCleaner.py
		words = dataCleaner.removeStopWords(dataCleaner.removeSpecialCharacters(tweet), num_grams)
		if tid in tid_dict:
			for token in selected_n_grams:
				if token in words:
					tdm_dict[tid][token]+=1




# writeCombinedFVtoARFF: writes the combined FV/ TDM to a .arff file
# arguments: path for .arff file, selected n_grams lists for both values of n, tdm dictionaries for both values of n, 
def writeCombinedFVtoARFF(out_file_path, selected_n_grams_n1,selected_n_grams_n2, tdm_dict_n1, tdm_dict_n2, tid_dict, sc_dict, header):
	
	fp = open(out_file_path, 'w')
	fp.write("@RELATION\t"+header+"\n")

	counter = 1
	for words in selected_n_grams_n1.keys():
		
		fp.write("@ATTRIBUTE\t"+str(counter)+"_")
		i=0
		tokens = words.split()
		# labeling the attribute properly
		for token in tokens:
			if i< len(tokens)-1:
				fp.write(str(token)+"_")
			else:
				fp.write(str(token))
			i+=1
		counter +=1
		fp.write("\tREAL\n")

	#counter = 1
	for words in selected_n_grams_n2.keys():
		
		fp.write("@ATTRIBUTE\t"+str(counter)+"_")
		i=0
		tokens = words.split()
		# labeling the attribute properly
		for token in tokens:
			if i< len(tokens)-1:
				fp.write(str(token)+"_")
			else:
				fp.write(str(token))
			i+=1
		counter +=1
		fp.write("\tREAL\n")
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
		for token in selected_n_grams_n1:
			fp.write(str(tdm_dict_n1[tid][token])+",")
		for token in selected_n_grams_n2:
			fp.write(str(tdm_dict_n2[tid][token])+",")
		# Objective tweets are considered as Neutral
		if tid_dict[tid] == 'objective':
			tid_dict[tid] = 'neutral'
		fp.write(tid_dict[tid])
		fp.write("\n")
	
	fp.close()

#### loading data from files - training and testing
loadDataFromFile(training_data_path + train_file, store_train_data, tweet_ids_train, sentiment_classes_train)

loadDataFromFile(testing_data_path + test_file, store_test_data, tweet_ids_test, sentiment_classes_test)

#### Unigrams 

## Training data 

ngramReader(store_train_data, n_grams_train_n1, 1)

chooseFrequentWords(n_grams_train_n1, selected_n_grams_train_n1, freq_thresh)

createFV(store_train_data, selected_n_grams_train_n1, tdm_train_n1, tweet_ids_train,1)

## Testing data 

ngramReader(store_test_data, n_grams_test_n1, 1)

createFV(store_test_data, selected_n_grams_train_n1, tdm_test_n1, tweet_ids_test, 1)


##### Bigrams


## Training data
ngramReader(store_train_data, n_grams_train_n2, 2)

chooseFrequentWords(n_grams_train_n2, selected_n_grams_train_n2, freq_thresh)

createFV(store_train_data, selected_n_grams_train_n2, tdm_train_n2, tweet_ids_train,2)


## Testing data
ngramReader(store_test_data, n_grams_test_n2, 2)

createFV(store_test_data, selected_n_grams_train_n2, tdm_test_n2, tweet_ids_test,2)


# ----------------------------------- Writing Combined ARFF : Training & Testing -------------------------------


writeCombinedFVtoARFF(arff_file_path+arff_train_file, selected_n_grams_train_n1, selected_n_grams_train_n2, tdm_train_n1, tdm_train_n2, tweet_ids_train, sentiment_classes_train, 'Sentiment_Analysis_Training_CombinedN-grams')

writeCombinedFVtoARFF(arff_file_path+arff_test_file, selected_n_grams_train_n1, selected_n_grams_train_n2, tdm_test_n1, tdm_test_n2, tweet_ids_test, sentiment_classes_train, 'Sentiment_Analysis_Testing_CombinedN-grams')
