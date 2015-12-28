# TDM_TA_uni.py
# Authors: Gerard Briones, Kasun Amarasinghe
# Creates the feature vector with unigrams
# TAsk : Given a tweet, clasify it to Neutral, positive or negative 

import csv
import dataCleaner

# data directory
data_path = 'data/'

# Arff file directory
arff_file_path = 'arff_data/'

# data file name
data_file = 'data_taskA.tsv'

# Arff for training
arff_file = 'TA_uni.arff'

# all words and frequencies in the training directory
unigrams = {}

# holds words with a pre defined frequency 
selected_unigrams = {}

# all tweet ids in the data set, stores the sentiment class as the value
tweet_ids = {}

# predefined freq threshold
# the minimum frequency a word should appear in the tweet to be selected
freq_thresh = 5

# dicts to hold the sentiment classes that exist and number of elements in each class (training and testing)
sentiment_classes = {'positive':0, 'neutral':0, 'negative':0} 

# The training and testing TDM/ FV
# TDM - Term Document Matrix, FV - Feature Vector
tdm = {}
tdm_tfIdf = {}

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
                        # first step, removing special characters other than ones related to smileys 
                                               
                        words = dataCleaner.removeStopWords(dataCleaner.removeSpecialCharacters(dataCleaner.convertEmoticons(tweet)),1)
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
                #words = dataCleaner.removeStopWords(dataCleaner.removeSpecialCharacters(dataCleaner.convertEmoticons(tweet)),1)
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

def getStats(n_grams, tid_dict, selected_n_grams, sc_dict):
    print 'Number of tweets: '
    print len(tid_dict)
    print '\ntotal words: '
    print len(n_grams)
    print '\nno_of_selected_words'
    print len(selected_n_grams)
    print '\nclass distribution: '
    print sc_dict

# Reading the training dataset
dataReader(data_path + data_file, unigrams, tweet_ids, sentiment_classes)

# Extracting words above frequency threshold 
chooseFrequentWords(unigrams, selected_unigrams, freq_thresh)

#printing stats
#getStats(unigrams, tweet_ids, selected_unigrams, sentiment_classes)

# Creating the FV/TDM
createFV(data_path + data_file, selected_unigrams, tdm, tweet_ids,  sentiment_classes)

# Writing FV/TDM to file
writeFVtoARFF(arff_file_path+arff_file, selected_unigrams, tdm, tweet_ids, sentiment_classes, 'Sentiment_Analysis_Baseline_TaskA')