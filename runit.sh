# runit.sh
# Authors: Gerard Briones
# runs the project

#!/bin/bash

#load the necessary data
python dataLoader.py

#create feature vector for baseline
python featureVectorCreator_BL.py

#run weka on baseline feature vector
java -Xmx2G -cp /usr/share/java/weka.jar weka.classifiers.bayes.NaiveBayes -o -t arff_data/arff_train_bl.arff -T arff_data/arff_test_bl.arff -k > output/weka_bl.txt

#create feature vector for pm (presented method)
python featureVectorCreator_PM.py

#run weka on pm feature vector
java -Xmx2G -cp /usr/share/java/weka.jar weka.classifiers.bayes.NaiveBayes -o -t arff_data/arff_train_pm.arff -T arff_data/arff_test_pm.arff -k > output/weka_pm.txt