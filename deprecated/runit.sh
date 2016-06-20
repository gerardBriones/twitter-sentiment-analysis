# runit.sh
# Authors: Gerard Briones
# runs the project

#!/bin/bash

# echo "Beginning Task A - 3 Point Classification"
echo "---| Welcome to the Twitter Sentiment Analyzer 3000! |---"
echo "---|   Authors: Gerard Briones, Kasun Amarasinghe    |---"

echo ""

echo "### Loading data..."
# load the necessary data for Task A
python TaskA/dataLoader_TaskA.py
echo "### Data for Task A has been loaded into data/ !"
# load the necessary data for Task B
python TaskB/dataLoader_TaskB.py
echo "### Data for Task B has been loaded into data/ !"

echo ""

echo "### Now creating arff's for Task A"
# create arff (baseline) for Task A
python TaskA/TDM_TA_uni.py
# create arff (stemming) for Task A
python TaskA/TDM_TA_stem.py
# create arff (emoticons + stemming) for Task A
python TaskA/TDM_TA_emot_stem.py
# create arff (emoticons + stemming + tf-idf) for Task A
python TaskA/TDM_TA_emot_stem_tfidf.py
echo "### arff's have been created for Task A! They can be found in arff/"

echo ""

echo "### Now creating arff's for Task B"
# create arff (baseline) for Task B
python TaskB/TDM_TB_uni.py
# create arff (stemming) for Task B
python TaskB/TDM_TB_stem.py
# create arff (emoticons + stemming) for Task B
python TaskB/TDM_TB_emot_stem.py
# create arff (emoticons + stemming + tf-idf) for Task B
python TaskB/TDM_TB_emot_stem_tfidf.py
echo "### arff's have been created for Task B! They can be found in arff/"

echo ""
echo "### Hopefully everything went smoothly. If not, blame Gerard, he's the one that wrote this."
echo ""
echo "### Ok, now to work some Weka magic!"
echo "### Note: this will be broken down in to multiple parts for each task. Please exercise some patience, these classifiers can be rather slow."
echo "### Output will be dumped into output/ ."
echo ""

echo "### Task A - Naive Bayes (NB) - BEGIN"
# -cp /usr/share/java/weka.jar # this is the class path for weka noobs
java -Xmx2G weka.classifiers.bayes.NaiveBayes -o -x -t arff_data/TA_uni.arff -k > output/TA_uni_NB_results.txt
java -Xmx2G weka.classifiers.bayes.NaiveBayes -o -x -t arff_data/TA_stem.arff -k > output/TA_stem_NB_results.txt
java -Xmx2G weka.classifiers.bayes.NaiveBayes -o -x -t arff_data/TA_emot_stem.arff -k > output/TA_emot_stem_NB_results.txt
java -Xmx2G weka.classifiers.bayes.NaiveBayes -o -x -t arff_data/TA_emot_stem_tfidf.arff -k > output/TA_emot_stem_tfidf_NB_results.txt
echo "### Task A - Naive Bayes (NB) - COMPLETE"

echo "### Task A - Naive Bayes Multinomial (NBM) - BEGIN"
java -Xmx2G weka.classifiers.bayes.NaiveBayesMultinomial -o -x -t arff_data/TA_uni.arff -k > output/TA_uni_NBM_results.txt
java -Xmx2G weka.classifiers.bayes.NaiveBayesMultinomial -o -x -t arff_data/TA_stem.arff -k > output/TA_stem_NBM_results.txt
java -Xmx2G weka.classifiers.bayes.NaiveBayesMultinomial -o -x -t arff_data/TA_emot_stem.arff -k > output/TA_emot_stem_NBM_results.txt
java -Xmx2G weka.classifiers.bayes.NaiveBayesMultinomial -o -x -t arff_data/TA_emot_stem_tfidf.arff -k > output/TA_emot_stem_tfidf_NBM_results.txt
echo "### Task A - Naive Bayes Multinomial (NBM) - COMPLETE"

echo "### Task A - J48 (J48) - BEGIN"
java -Xmx2G weka.classifiers.trees.J48 -o -x -t arff_data/TA_uni.arff -k > output/TA_uni_J48_results.txt
java -Xmx2G weka.classifiers.trees.J48 -o -x -t arff_data/TA_stem.arff -k > output/TA_stem_J48_results.txt
java -Xmx2G weka.classifiers.trees.J48 -o -x -t arff_data/TA_emot_stem.arff -k > output/TA_emot_stem_J48_results.txt
java -Xmx2G weka.classifiers.trees.J48 -o -x -t arff_data/TA_emot_stem_tfidf.arff -k > output/TA_emot_stem_tfidf_J48_results.txt
echo "### Task A - J48 (J48) - COMPLETE"

echo "### Task B - Naive Bayes (NB) - BEGIN"
java -Xmx2G weka.classifiers.bayes.NaiveBayes -o -x -t arff_data/TB_uni.arff -k > output/TB_uni_NB_results.txt
java -Xmx2G weka.classifiers.bayes.NaiveBayes -o -x -t arff_data/TB_stem.arff -k > output/TB_stem_NB_results.txt
java -Xmx2G weka.classifiers.bayes.NaiveBayes -o -x -t arff_data/TB_emot_stem.arff -k > output/TB_emot_stem_NB_results.txt
java -Xmx2G weka.classifiers.bayes.NaiveBayes -o -x -t arff_data/TB_emot_stem_tfidf.arff -k > output/TB_emot_stem_tfidf_NB_results.txt
echo "### Task B - Naive Bayes (NB) - COMPLETE"

echo "### Task B - J48 (J48) - BEGIN"
java -Xmx2G weka.classifiers.trees.J48 -o -x -t arff_data/TB_uni.arff -k > output/TB_uni_J48_results.txt
java -Xmx2G weka.classifiers.trees.J48 -o -x -t arff_data/TB_stem.arff -k > output/TB_stem_J48_results.txt
java -Xmx2G weka.classifiers.trees.J48 -o -x -t arff_data/TB_emot_stem.arff -k > output/TB_emot_stem_J48_results.txt
java -Xmx2G weka.classifiers.trees.J48 -o -x -t arff_data/TB_emot_stem_tfidf.arff -k > output/TB_emot_stem_tfidf_J48_results.txt
echo "### Task B - J48 (J48) - COMPLETE"

echo ""
echo "### Normally, this is when we'd run Task B through the SMO classifier, but seeing as it takes a long time, we've decided to comment it out."
echo "### If you'd like to still run it, uncomment lines 96 - 101 in runit.sh"
echo ""

# echo "### Task B - SMO (SMO) - BEGIN"
# java -Xmx2G weka.classifiers.functions.SMO -o -x -t arff_data/TB_uni.arff -k > output/TB_uni_SMO_results.txt
# java -Xmx2G weka.classifiers.functions.SMO -o -x -t arff_data/TB_stem.arff -k > output/TB_stem_SMO_results.txt
# java -Xmx2G weka.classifiers.functions.SMO -o -x -t arff_data/TB_emot_stem.arff -k > output/TB_emot_stem_SMO_results.txt
# java -Xmx2G weka.classifiers.functions.SMO -o -x -t arff_data/TB_emot_stem_tfidf.arff -k > output/TB_emot_stem_tfidf_SMO_results.txt
# echo "### Task B - SMO (SMO) - COMPLETE"

echo ""
echo "### Aw yis, PHASE 2!"
echo "### BEGIN CHARGING THE VOTING LASERS!"
echo "Note: this will take longer than running a single classifier, so please be patient."
echo ""

echo "### Task A - Voting (Naive Bayes, Naive Bayes Multinomial, J48) - BEGIN"
java -Xmx2G weka.classifiers.meta.Vote -o -x -t arff_data/TA_uni.arff -B weka.classifiers.bayes.NaiveBayes -B weka.classifiers.bayes.NaiveBayesMultinomial -B weka.classifiers.trees.J48 -R MAJ -k > output/TA_uni_VOT_results.txt
java -Xmx2G weka.classifiers.meta.Vote -o -x -t arff_data/TA_stem.arff -B weka.classifiers.bayes.NaiveBayes -B weka.classifiers.bayes.NaiveBayesMultinomial -B weka.classifiers.trees.J48 -R MAJ -k > output/TA_stem_VOT_results.txt
java -Xmx2G weka.classifiers.meta.Vote -o -x -t arff_data/TA_emot_stem.arff -B weka.classifiers.bayes.NaiveBayes -B weka.classifiers.bayes.NaiveBayesMultinomial -B weka.classifiers.trees.J48 -R MAJ -k > output/TA_emot_stem_VOT_results.txt
java -Xmx2G weka.classifiers.meta.Vote -o -x -t arff_data/TA_emot_stem_tfidf.arff -B weka.classifiers.bayes.NaiveBayes -B weka.classifiers.bayes.NaiveBayesMultinomial -B weka.classifiers.trees.J48 -R MAJ -k > output/TA_emot_stem_tfidf_VOT_results.txt
echo "### Task A - Voting (Naive Bayes, Naive Bayes Multinomial, J48) - COMPLETE"

echo ""
echo "### So, this is where we'd run voting on Task B. We are not going to do that though, it takes over an hour to complete a single arff and ain't nobody got time for that. It has been commented out."
echo "### However, if you'd still like to run it, uncomment lines 122 - 127 in runit.sh"
echo "### Do this at your own risk, however. This process is extremely RAM hungry and can/will lock up your computer."
echo ""

# echo "### Task B - Voting (Naive Bayes, J48, SMO) - BEGIN"
# java -Xmx2G weka.classifiers.meta.Vote -o -x -t arff_data/TB_uni.arff -B weka.classifiers.bayes.NaiveBayes -B weka.classifiers.trees.J48 -B weka.classifiers.functions.SMO -R MAJ -k > output/TB_uni_VOT_results.txt
# java -Xmx2G weka.classifiers.meta.Vote -o -x -t arff_data/TB_stem.arff -B weka.classifiers.bayes.NaiveBayes -B weka.classifiers.trees.J48 -B weka.classifiers.functions.SMO -R MAJ -k > output/TB_stem_VOT_results.txt
# java -Xmx2G weka.classifiers.meta.Vote -o -x -t arff_data/TB_emot_stem.arff -B weka.classifiers.bayes.NaiveBayes -B weka.classifiers.trees.J48 -B weka.classifiers.functions.SMO -R MAJ -k > output/TB_emot_stem_VOT_results.txt
# java -Xmx2G weka.classifiers.meta.Vote -o -x -t arff_data/TB_emot_stem_tfidf.arff -B weka.classifiers.bayes.NaiveBayes -B weka.classifiers.trees.J48 -B weka.classifiers.functions.SMO -R MAJ -k > output/TB_emot_stem_tfidf_VOT_results.txt
# echo "### Task B - Voting (Naive Bayes, J48, SMO) - COMPLETE"