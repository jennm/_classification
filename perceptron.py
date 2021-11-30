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

    def train( self, trainingData, trainingLabels, validationData, validationLabels ):
        """
        The training loop for the perceptron passes through the training data several
        times and updates the weight vector for each label based on classification errors.
        See the project description for details.

        Use the provided self.weights[label] data structure so that
        the classify method works correctly. Also, recall that a
        datum is a counter from features to values for those features
        (and thus represents a vector a values).
        """

        self.features = trainingData[0].keys() # could be useful later
        # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
        # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.

        # self.classify([])
        # print "training data", len(trainingData[0].keys())
        # print "labels", trainingLabels
        # print "validation data", validationData
        # print "validation labels", validationLabels
        # print "features", self.features
        # print "weights", self.weights
        # return


        self.score = util.Counter()
        for f in self.features:
            self.score[f] = util.Counter()
            for y in range(len(self.weights)):
                self.score[f][y] = list()
        # self.score = [util.Counter()] * len(self.features)

        for iteration in range(self.max_iterations):
            # print "Starting iteration ", iteration, "..."
            # guesses = self.classify(trainingData)
            # print guesses
            for i in range(len(trainingData)):

                # print list(trainingData[i])
                features = trainingData[i].keys()
                for feature in features:
                    self.weights[trainingData[i][feature]][feature] += 1 

            classified = self.classify(trainingData)
            # print len(classified)
            # print len(features)
            for j in range(len(classified)):
                # print trainingData[i][features[j]]
                if classified[j] == trainingLabels[j]:
                    continue
                else:
                    feat_weight = trainingLabels[j]
                    # print features[i]
                    for k in range(len(self.weights[trainingLabels[j]])):
                        self.weights[trainingLabels[j]][k] += feat_weight
                    for k in range(len(self.weights[classified[j]])):
                        self.weights[classified[j]][k] -= feat_weight
                        # print "else"

            # self.classify()
                # max_guesses = self.classify(list(trainingData[i]))
                # print len(list())
                # print max_guesses

                # for feature in self.features:
                #     score = list()
                #     for y in range(len(self.weights)):
                #         tmp = 0
                #         # for 
                #         # score.
                # # print len(self.weights)
                # return

                # break
                



                # pass
                # guesses = self.classify(trainingData[i])
                # print guesses



                # for y in range(len(self.weights)):

                #     for feature in self.features:
                #         tmp = 0
                #         for i in range(len(feature)):
                #             tmp += feature[i] * self.weights[y][i]

                #         # print self.score[feature][y]
                #         # if self.score[feature][y] == 0:
                #         #     self.score[feature][y] = [tmp]
                #         # else:
                #         self.score[feature][y].append(tmp)

                    # print self.score
                    # print self.features
                    # print self.weights
                    # tmp = 0
                    # for index in range(len(self.features[y])):
                    #     tmp += self.features[y][index] * self.weights[y][index]
                    # self.score[y][self.features[y]] = tmp
                    # self.score[y][self.features[i]] += self.features[i] * self.weights[y] 
                # "*** YOUR CODE HERE ***"
                    # util.raiseNotDefined()
            return
            # print self.weights
            max_y = -1
            print self.weights
            for feature in self.features:
                max_score = self.score[feature][0]
                max_y = 0
                for y in range(len(self.weights)):
                    for s in self.score[feature][y]:
                        if s > max_score:
                            max_score = s
                            max_y = y
                for y in range(len(self.weights)):

                    # if max_y < 0:
                    #     for s in self.score[feature][y]:
                    #         if s > max_score:
                    #             max_score = s
                    #             max_y = y

                    # print "pre", feature
                    if y == max_y:# or max_y < 0:
                        continue
                    # print feature
                    for index in range(len(feature)):
                        # print feature
                        self.weights[y][index] += feature[i]
                        self.weights[max_y][index] -= feature[i]

            print self.weights
            return self.weights



        # for y in range(len(self.weights)):
        #     max = 0
        #     feat = 0
        #     for i in range(len(trainingData)):
        #         tmp = self.score[y][self.features[i]]
        #         if tmp > max:
        #             max = tmp
        #             feat = i
            
        #     for i in range(len(trainingData)):
        #         print "hi", i
        #         if i == feat:
        #             continue
        #         # print self.weights
        #         # if self.weights[i] == 0:
        #         #     self.weights[i] = self.features[i]
        #         # else:
        #         for index in range(len(self.features[i])):
        #             self.weights[y][index] += self.features[i][index]
        #             # self.weights[i] += self.features[i]
        #         # if self.weights[feat] == 0:
        #         #     self.weights[feat] = -1 * self.features[i]
        #         # else:
        #         for index in range(len(self.features[i])):
        #             self.weights[y][index] -= self.features[i][index]
                    
    def classify(self, data ):
        """
        Classifies each datum as the label that most closely matches the prototype vector
        for that label.  See the project description for details.

        Recall that a datum is a util.counter...
        """
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
