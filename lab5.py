#!/usr/local/python-2.7.5/bin/python

""" lab2.py
    -------
    @author = Ankai Lou
"""

###############################################################################
############## modules & libraries required for the KDD process ###############
###############################################################################

import sys
import time

###############################################################################
####### modules for the KDD process (proprocessing, classification, etc) ######
###############################################################################

from preprocessing import preprocessing
from minwisehash import minwisehash

###############################################################################
################## main function = single point of execution ##################
###############################################################################

def main(argv):
    """ function: main
        --------------
        KDD process for Reuter article database

        :param argv: commend line arguments
    """
    start_time = time.time()

# Preprocessing =
    # 1. Text Extraction
    # 2. Feature Selection
    # 3. Feature Vector Generation
    print('Step 1: Preprocessing')
    fv = preprocessing.begin()

    # Minhash for k = 16, 32, 64, 128, 256
    print('\nStep 2: K-Minwise Hashing:')
    minwisehash.begin(fv)

    # Report Total Running Time
    end_time = time.time() - start_time
    print '\nProcess finished in', end_time, 'seconds!'

if __name__ == '__main__':
    main(sys.argv[1:])
