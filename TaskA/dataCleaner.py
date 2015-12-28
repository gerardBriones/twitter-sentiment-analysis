# dataCleaner.py
# Author: Kasun Amarasinghe
# removes special characters, lower casifies the data, and removes stop words

import re

supporting_data_path = "supporting_data/"

# Author: Kasun Amarasinghe
# perform initial preprocessing
# returns all lower case string without special characters, numbers etc. 
def removeSpecialCharacters(str):
	new_str = re. sub('[^A-Za-z ]+', '', str) # retaining the punctuation needed for smileys
	new_str = new_str.lower()
	return new_str 
 
# Authors: Kasun Amarasinghe, Gerard Briones
# Removes stop words from the string
# Before calling this method, initial_preprocessing has to be called
# pass in the initial preprocessed string as the argument
# returns the tokens sans stop words from the tweet
def removeStopWords(str, n):
	stopWord_Filename = "stopWord_list.txt"

	# stop words should be space delimited
	sw_fp = open(supporting_data_path + stopWord_Filename)
	for row in sw_fp:
		row = re. sub('[^A-Za-z ]+', '', row)
		sw_list = row.split()

	# extracting the set of words in the string 	
	word_list = str.split();
	key_words = []
	for word in word_list:
		if word not in sw_list:
			key_words.append(word)

	##AUTHORSHIP NOTE
	# -- This code block was handled by Gerard Briones --
	# build ngrams from key_words
	ngrams = []
	for i in range(0, len(key_words)):
		temp_string = ''
		if (i + n - 1) >= len(key_words):
			break;
		for j in range(i, i + n):
			if j >= len(key_words):
				break;
			temp_string += (key_words[j]) + ' '
		ngrams.append(temp_string.rstrip())
	return ngrams

# Author: Gerard Briones
# convert emoticons to unique words
def convertEmoticons(str):
	# matches variations of :) -- smileEmoticon
	str = re.sub('[:=8]-?[)\]}]|[([{}]-?[:=8]', 'smileEmoticon', str)

	# matches variations of :( -- frownEmoticon
	str = re.sub('[:=8]-?[([{]|[)\]}]-?[:=8]', 'frownEmoticon', str)

	# matches variations of ;) -- winkEmoticon
	str = re.sub(';-?[)\]}]|[([{}]-?;', 'winkEmoticon', str)

	# matches variations of :P
	str = re.sub('[:=;8]-?[pP]|[dpP]-?[:=;8]', 'tongueEmoticon', str)

	# matches variations of :/
	str = re.sub('[:=;8]-?[/|\\\]|[/|\\\]-?[:=;8]', 'concernEmoticon', str)

	# matches variations of :D
	str = re.sub('[:=xX8]-?D', 'grinEmoticon', str)
	
	# matches variations of D:
	str = re.sub('D-?[:=xX8]', 'mirrorGrinEmoticon', str)

	# matches variations of ;D
	str = re.sub(';-?D', 'winkGrinEmoticon', str)

	# matches variations of :O
	str = re.sub('[:=]-?[oO]|[oO]-?[:=]', 'surpriseEmoticon', str)

	# matches variations of :')
	str = re.sub('[:=][\'`]-?[)\]}]|[([{]-?[\'`][:=]', 'tearSmileEmoticon', str)

	# matches variations of :'(
	str = re.sub('[:=][\'`]-?[({[]|[)\]}]-?[\'`][:=]', 'tearFrownEmoticon', str)

	return str