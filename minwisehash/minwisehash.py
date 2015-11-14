#!/usr/local/python-2.7.5/bin/python

""" minwisehash.py
    --------------
    @author = Ankai Lou
"""

###############################################################################
###### modules required for computing jaccard similarity and minwish hash #####
###############################################################################

import time
import math
import random

###############################################################################
############################### global variables ##############################
###############################################################################

num_hashes = [16, 32, 64, 128, 256]

###############################################################################
################# strings representing classifier experiments #################
###############################################################################

fv_dataset_name = ["standard feature vector","pared feature vector"]

###############################################################################
############ helper function(s) for generating jaccard similarity #############
###############################################################################

def __jaccard_similarity(v1, v2, version):
    """ function: jaccard_similarity
        ----------------------------
        calculate jaccard similarity of two boolean vectors

        :param v1: first boolean feature vector
        :param v2: second boolean feature vector
        :param version: 0 = baseline, 1 = minhash
        :returns: similarity score for @v1 and @v2
    """
    union = 0 # (0,1), (1,0), (1,1)
    inter = 0 # (1,1)
    if version == 0:
        for i, j in zip(v1, v2):
            union += i | j
            inter += i & j
    elif version == 1:
        union += len(set(v1) | set(v2))
        inter += len(set(v1) & set(v2))
    return 0.0 if union == 0 else inter / float(union)

###############################################################################
############ helper function(s) for generating similarity matrices ############
###############################################################################

def __generate_similarity_matrix(dataset, version):
    """ function: baseline
        ------------------
        calculate baseline raw jaccard similarity for dataset

        :param dataset: set of feature vectors representing documents
        :param version: 0 = baseline, 1 = minhash
        :returns: matrix representing jaccard similarity scores
    """
    baseline_matrix = dict([])
    # iterate pairwise through matrix
    for i, v1 in dataset.iteritems():
        for j, v2 in dataset.iteritems():
            # cut computations in half
            if i < j:
                tmp = __jaccard_similarity(v1, v2, version)
                # initialize inner dict if necessary
                if not baseline_matrix.has_key(i):
                    baseline_matrix[i] = dict([])
                # add jaccard similarity score to baseline matrix
                baseline_matrix[i][j] = tmp
    return baseline_matrix

def __generate_signatures(dataset,permutations):
    """ function: generate_signatures
        -----------------------------
        generate signatures for @dataset given hash functions

        :param dataset: set of feature vectors
        :param permutations: hash functions to run
        :returns: dict of (document, list) signatures
    """
    signatures = dict([])
    for i, fv in dataset.iteritems():
        # int list of size = k
        signature = []
        for hash in permutations:
            for index in hash:
                if fv.vector[index] == 1:
                    signature.append(index)
                    break
        # save signature for document
        signatures[i] = signature
    return signatures

def __error(minhash, baseline):
    """ function: error
        ---------------
        calculate mean-squared error between two similarity matrices

        :param minhash: similarity matrix for minwish hash results
        :param baseline: similarity matrix for baseline dataset
        :returns: float representing error
    """
    error = 0.0
    for i, row in baseline.iteritems():
        for j, score in row.iteritems():
            error += (score - minhash[i][j]) ** 2
    return math.sqrt(error)

###############################################################################
################# main function for single-point-of-execution #################
###############################################################################

def begin(feature_vectors):
    """ function: begin
        ---------------
        generate baseline and k-minwise similarity estimates

        :param feature_vectors: standard dataset generated using tf-idf
    """
    # iterate across feature vector sets
    for i, dataset in enumerate(feature_vectors):
        # get number of feature vector in dataset
        num_features = len(dataset[0].vector)

        # generate baseline jaccard similarity matrix
        print "\nGenerating baseline for", fv_dataset_name[i], "(this may take time)"
        # flatten the dataset
        flat = { i : fv.vector for i,fv in dataset.iteritems() }
        start_time = time.time()
        baseline_sim = __generate_similarity_matrix(flat,0)
        end_time = time.time() - start_time
        print "Generated baseline matrix in", end_time, 'seconds!'

        # generate minwise hash sketches
        permutations = []
        for k in num_hashes:
            # generate up to k hash functions
            while len(permutations) < k:
                hash = range(0,num_features)
                random.shuffle(hash)
                # add if not previously generated
                if hash not in permutations:
                    permutations.append(hash)
            # generate document signatures for permutations
            print "\nGenerating signatures for minhash sketch for k =", k
            start_time = time.time()
            signatures = __generate_signatures(dataset,permutations)
            # generate similarity score matrix for signatures
            print "Generating similarity for minhash sketch for k =", k
            minhash_sim = __generate_similarity_matrix(signatures,1)
            end_time = time.time() - start_time
            # generate total error between minhash and baseline
            print "Error for minwise hashing sketch for k =", k, ":", __error(baseline_sim, minhash_sim)
            print "Minwise hash sketch for k =", k, "finished in", end_time, "seconds!"
