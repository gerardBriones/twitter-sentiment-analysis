# dataCleaner.py
# removing special characters and lower casifying the data

import re

supporting_data_path = "supporting_data/"


# perform initial preprocessing
# returns all lower case string without special characters, numbers etc. 
def removeSpecialCharacters(str):
	new_str = re. sub('[^A-Za-z ]+', '', str)
	new_str = new_str.lower()
	return new_str 

# Removes stop words from the string
# Before calling this method, initial_preprocessing has to be called
# pass in the initial preprocessed string as the argument
# returns the tokens sans stop words from the tweet
def removeStopWords(str):
	# extracting the set of words in the string 	
	word_list = str.split();

	stopWord_Filename = "stopWord_list.txt"

	# stop words should be space delimited
	sw_fp = open(supporting_data_path + stopWord_Filename)
	for row in sw_fp:
		row = re. sub('[^A-Za-z ]+', '', row)
		sw_list = row.split()
	word_list = str.split();
	key_words = []
	for word in word_list:
		if word not in sw_list:
			key_words.append(word)
	return key_words
