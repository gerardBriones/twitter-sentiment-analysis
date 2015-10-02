# runit.sh
# Authors: Gerard Briones
# runs the project

#!/bin/bash

#load the necessary data
python dataLoader.py

#create feature vector for baseline
python featureVectorCreator_BL.py

#run naive bayes on baseline feature vector
java -Xmx2G -cp /usr/share/java/weka.jar weka.classifiers.bayes.NaiveBayes -o -t arff_data/arff_train_bl.arff -T arff_data/arff_test_bl.arff -k > output/naiveBayes_bl.txt

#run naive bayes multinomial on baseline feature vector
java -Xmx2G -cp /usr/share/java/weka.jar weka.classifiers.bayes.NaiveBayesMultinomial -o -t arff_data/arff_train_bl.arff -T arff_data/arff_test_bl.arff -k > output/naiveBayesMulti_bl.txt

#run decision tree J48 on baseline feature vector
java -Xmx2G -cp /usr/share/java/weka.jar weka.classifiers.trees.J48 -o -t arff_data/arff_train_bl.arff -T arff_data/arff_test_bl.arff -k > output/j48_bl.txt

#run decision tree random forst on baseline feature vector
java -Xmx2G -cp /usr/share/java/weka.jar weka.classifiers.trees.RandomForest -o -t arff_data/arff_train_bl.arff -T arff_data/arff_test_bl.arff -k > output/randomForest_bl.txt

#create feature vector for pm (presented method)
python featureVectorCreator_PM.py

#run naive bayes on pm feature vector
java -Xmx2G -cp /usr/share/java/weka.jar weka.classifiers.bayes.NaiveBayes -o -t arff_data/arff_train_pm.arff -T arff_data/arff_test_pm.arff -k > output/naiveBayes_pm.txt

#run naive bayes multinomial on pm feature vector
java -Xmx2G -cp /usr/share/java/weka.jar weka.classifiers.bayes.NaiveBayesMultinomial -o -t arff_data/arff_train_pm.arff -T arff_data/arff_test_pm.arff -k > output/naiveBayesMulti_pm.txt

#run decision tree J48 on pm feature vector
java -Xmx2G -cp /usr/share/java/weka.jar weka.classifiers.trees.J48 -o -t arff_data/arff_train_pm.arff -T arff_data/arff_test_pm.arff -k > output/j48_pm.txt

#run decision tree random forst on pm feature vector
java -Xmx2G -cp /usr/share/java/weka.jar weka.classifiers.trees.RandomForest -o -t arff_data/arff_train_pm.arff -T arff_data/arff_test_pm.arff -k > output/randomForest_pm.txt

#create feature vector of combined unigrams and bigrams
python featureVectorCreator_combined.py

#run naive bayes on combined feature vector
java -Xmx2G -cp /usr/share/java/weka.jar weka.classifiers.bayes.NaiveBayes -o -t arff_data/arff_train_combined.arff -T arff_data/arff_test_combined.arff -k > output/naiveBayes_combined.txt

#run naive bayes multinomial on combined feature vector
java -Xmx2G -cp /usr/share/java/weka.jar weka.classifiers.bayes.NaiveBayesMultinomial -o -t arff_data/arff_train_combined.arff -T arff_data/arff_test_combined.arff -k > output/naiveBayesMulti_combined.txt

#run decision tree J48 on combined feature vector
java -Xmx2G -cp /usr/share/java/weka.jar weka.classifiers.trees.J48 -o -t arff_data/arff_train_combined.arff -T arff_data/arff_test_combined.arff -k > output/j48_combined.txt

#run decision tree random forest on combined feature vector
java -Xmx2G -cp /usr/share/java/weka.jar weka.classifiers.trees.RandomForest -o -t arff_data/arff_train_combined.arff -T arff_data/arff_test_combined.arff -k > output/randomForest_combined.txt
