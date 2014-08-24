                                  Readme
---------------------------------------------------------------------------

What it is
----------

Using the structure of ClassifierStructure.h, I have completed the class
definitions in python.

Use the same datasets performed 5-fold cross-validation on each dataset. 
i.e., divide the dataset into 5 non-overlapping partitions (using the 
splitDataset() function) and in each fold, test using one of the folds 
while training using the other four. Reported the average error, standard 
deviation of error and the confusion matrix.

Implemented the above using the given strategies in the classifier structure 
given different learning algorithms and different combination strategies. 

Aim
---

The goal of this project is develop an understanding of the design of feature 
extractors, and selection of classification algorithms. The design/selection 
of features and classifiers depend on the nature of the dataset

A. Distance based classifiers
1. Single Nearest Neighbor
2. k-Nearest Neighbor
3. Weighted k-NN
4. Nearest Mean
For each of the distance based classifiers, use Euclidean, Manhattan and Minkowski 
distance metrics to carry out the analysis mentioned below.

B. Linear Classifiers
Implement linear classifiers that learn using the following methods.
1) Perceptron Learning:
a) Batch learning
b) Single sample Fixed increment, and
c) Single sample Variable increment with margin.
2) Minimum Squared error classifier using Pseudoinverse method. 
3) LMS procedure for minimum squared error learning.

Linear classifiers are meant for two-class classification. However, most of the 
datasets provided below contain more than two classes. Use one of the strategies
mentioned in the class to combine multiple two-class classifiers into a single
multi-class classifier.

Iris Dataset: A simple classic 3-class dataset with 4
features and 50 samples from each class. Download
from: http://archive.ics.uci.edu/ml/datasets/Iris

Wine: Another simple 3-class dataset. Download from:
http://archive.ics.uci.edu/ml/datasets/Wine

