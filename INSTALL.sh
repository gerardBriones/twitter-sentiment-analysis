# INSTALL.sh
# Authors: Gerard Briones
# script to install the dependencies of the project
#
# SciPy stack - http://www.scipy.org/
# pip - https://docs.python.org/2/installing/
# NLTK - http://www.nltk.org/index.html
# SciKit - http://scikit-learn.org/stable/

#!/bin/bash
echo "--- Installing the SciPy stack! (http://www.scipy.org/) ---"
sudo apt-get install python-setuptools python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

echo "--- Installing pip (https://docs.python.org/2/installing/) ---"
sudo easy_install pip

echo "--- Installing NLTK (http://www.nltk.org/index.html) ---"
sudo pip install -U nltk

echo "--- Installing NLTK data (http://www.nltk.org/data.html) ---"
python -m nltk.downloader all

echo "--- Installing SciKit (http://scikit-learn.org/stable/) ---"
sudo pip install -U scikit-learn