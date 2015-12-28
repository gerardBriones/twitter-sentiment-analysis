# dataLoader.py : Task B
# Authors: Gerard Briones, Kasun Amarasinghe
# retains the important dimensions of the tweet 

import csv
import os

# directory with all data
all_data_path = 'data_all/'

# directory to store data
data_path = 'data/'
if not os.path.exists(data_path):
    os.makedirs(data_path)

# directory to store arffs
arff_data_path = 'arff_data/'
if not os.path.exists(arff_data_path):
    os.makedirs(arff_data_path)

# directory to store output
output_path = 'output/'
if not os.path.exists(output_path):
    os.makedirs(output_path)

# keeping track of number of records
num_records = 0

# dictionary to keep track of tweet_ids
# eliminate duplicate tweets in data set
tweet_ids = {}

filename = 'TaskBD.tsv'
    
# defining the files to store the train and test datas
data_file = 'data_taskB.tsv'
    
fp = open(data_path+data_file,'w')

with open(all_data_path + filename, 'rb') as tsv_in:
    
    tsv_in = csv.reader(tsv_in, delimiter='\t')

    # ROW PATTERN - One tweet per line
    # ID | TOPIC | SENTIMENT | TWEET
    for row in tsv_in:
        tid = row[0]
        
        # checking for duplicates
        if not tid in tweet_ids:
            tweet_ids[tid] = 1
            topic = row[1]
            tweet = row[3]
            # checking for empty tweets
            if tweet=='Not Available':    
                pass 

            ##AUTHORSHIP NOTE
            # -- This code block is mostly handled by Kasun --
            else:
                sentiment = row[2]
                fp.write(str(tid)+"\t"+topic+"\t"+tweet+"\t"+sentiment+"\n")
                num_records +=1

fp.close()