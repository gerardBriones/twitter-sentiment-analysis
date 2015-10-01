# dataLoader.py
# Authors: Gerard Briones, Kasun Amarasinghe
# splits the large data set into 60% training and 40% testing

import csv
import os
import random

# directory with all data
all_data_path = 'data_all/'

# directory to store training data
train_data_path = 'train_data/'

# directory to store testing data
test_data_path = 'test_data/'

# setting training and testing percentages
training_portion = 60
testing_portion = 100 - training_portion

# keeping track of number of training records and testing records
num_training = 0
num_testing = 0

# dictionary to keep track of tweet_ids
# eliminate duplicate tweets in data set
tweet_ids = {}

for filename in os.listdir(all_data_path):
	
	# defining the files to store the train and test datas
	train_data_file = 'train_data_taskA.tsv'
	test_data_file = 'test_data_taskA.tsv'
	
	fp_train = open(train_data_path+train_data_file,'w')
	fp_test = open(test_data_path+test_data_file, 'w')

	with open(all_data_path + filename, 'rb') as tsv_in:
		
		tsv_in = csv.reader(tsv_in, delimiter='\t')

		for row in tsv_in:
			tid = row[0]
			
			# checking for duplicates
			if not tid in tweet_ids:
				tweet_ids[tid] = 1
				tweet = row[5]
				# checking for empty tweets
				if tweet=='Not Available':	
					pass
				else:
					sentiment = row[4]
						
					# creating a random number between 0 and 100
					num = random.uniform(0,100)
					if num < training_portion:
						fp_train.write(str(tid)+"\t"+tweet+"\t"+sentiment+"\n")
						num_training +=1
					else:
						fp_test.write(str(tid)+"\t"+tweet+"\t"+sentiment+"\n")
						num_testing +=1
			
	



	#print num_training, num_testing
	fp_train.close()
	fp_test.close()
				

