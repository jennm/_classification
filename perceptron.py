# perceptron.py
# -------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# Perceptron implementation
from random import triangular
import util
PRINT = True

class PerceptronClassifier:
    """
    Perceptron classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        print "LegalLabels", self.legalLabels
        self.type = "perceptron"
        self.max_iterations = max_iterations
        self.weights = {}
        for label in legalLabels:
            self.weights[label] = util.Counter() # this is the data-structure you should use

    def setWeights(self, weights):
        assert len(weights) == len(self.legalLabels);
        self.weights = weights;

    def train(self, input_train_data, label_train_data, input_val_data, label_val_data):
        """
        Question 1: Implement the multi-class version of the perceptron algorithm

        Args:
            input_train_data: list of util.Counters
            label_train_data: list of integers (representing the labels) of the same length as input_train_data
            input_val_data: list of util.Counters
            label_val_data: list of integers (representing the labels) of the same length as input_val_data
            iterations: number of iterations to pass over all the dataset
            callback: callback function for plotting

        The training loop for the perceptron passes through the training data
        several times and updates the weight vector for each label based on
        classification errors. See the project description for details.

        Use the provided self.weights[label] data structure so that
        the classify method works correctly. Also, recall that a
        datum is a counter from features to values for those features
        (and thus represents a vector a values).

        You don't need to use the validation data (input_val_data, label_val_data)
        for this question, but it is provided in case you want to check the
        accuracy on the validation data.

        Useful method:
        self.classify(...)
        """

        # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
        # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.
        for iteration in range(self.max_iterations):
            print "Starting iteration ", iteration, "..."
            # print input_train_data[0]
            # for i in range(len(input_train_data)):
            # score = util.Counter()
            # for k in self.weights.keys():

            
            for i in range(len(input_train_data)):

                score = util.Counter()
                for weight in self.weights.keys():
                    score[weight] = self.weights[weight] * input_train_data[i]

                max_y = score.argMax()

                if max_y != label_train_data[i]:
                    self.weights[label_train_data[i]] += input_train_data[i]
                    self.weights[max_y] -= input_train_data[i]


    def classify(self, data ):
        """
        Classifies each datum as the label that most closely matches the prototype vector
        for that label.  See the project description for details.

        Recall that a datum is a util.counter...
        """
        # print data
        guesses = []
        for datum in data:
            vectors = util.Counter()
            for l in self.legalLabels:
                vectors[l] = self.weights[l] * datum
            guesses.append(vectors.argMax())
        return guesses


    def findHighWeightFeatures(self, label):
        """
        Returns a list of the 100 features with the greatest weight for some label
        """
        featuresWeights = []

        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

        return featuresWeights
