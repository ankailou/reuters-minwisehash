Lab 5 - Minwise Hashing
=======================

## Table of Contents
1. [Overview](#overview)
2. [Module Description](#description)
3. [Usage](#usage)
4. [Development](#development)
5. [Change Log](#change-log)

## Overview
The purpose of this module is to implement minwise hashing for estimating document similarity on the feature vectors generated in lab 1. This module is built on the preprocessing module that sanitized a set of SGML documents representing a Reuters article database into a dataset of feature vectors and class labels. The results of the clustering algorithms will be employed in future assignments for automated categorization, similarity search, and building document graphs.

## Description
This python module contains the following files and directories:

* lab2.py - main module for KDD process
* preprocessing/
    * \_\_init\_\_.py
    * preprocessing.py - module for preprocessing the Reuters article database
    * document/
        * \_\_init\_\_.py
        * document.py - sub-module for text extraction & tokenization of document objects
    * lexicon/
        * \_\_init\_\_.py
        * lexicon.py - sub-module for generating the title/body lexicon for document set 
    * feature/
        * \_\_init\_\_.py
        * feature.py - sub-module for generating feature vector datasets
        * weighting.py - sub-module for computing tf-idf scores
        * featureselect.py - sub-module for feature selection/reduction
* minwisehash/
    * \_\_init\_\_.py
    * minwisehash - submodule for performing minwise hashing
* data/
    * reut2-xxx.sgm - formatted articles (replace xxx from {000,...,021})

The `preprocessing.py` file will generate the following files

* dataset1.csv - regular feature vector set
* dataset2.csv - pared down version of feature vector in dataset1.csv

The feature vectors in the datasets were generated using the following methodologies

* TF-IDF of title & body words to select the top 5 words of each document features
* Feature reduction process of paring down original feature vector to 10% original size

Potential additional to future iterations of feature vector generation:

* different normalization
* bigram/trigram/n-gram aggregation
* stratified sampling: starting letter, stem, etc.
* binning: equal-width & equal-depth (grouping by topics/places, part-of-speech, etc)
* entropy-based discretization (partitioning based on entropy calculations)

For more information on the implementation and the offline/online costs and accuracy, see:

```
> report5.pdf
```

## Usage
This module relies on several libraries to perform preprocessing, before anything:

Ensure NLTK is installed and the corpus and tokenizers are installed:

```
> pip install NLTK
```

Next, enter a Python shell and download the necessary NLTK data:

```
> python
$ import nltk
$ nltk.download()
```

From the download window, ensure `punkt`, `wordnet` and `stopwords` are downloaded onto your machine.

```
---------------------------------------------------------------------------
    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
---------------------------------------------------------------------------
Downloader> d
Download which package (l=list; x=cancel)?
  Identifier> punkt
    Downloading package punkt to /home/3/loua/nltk_data...
      Unzipping tokenizers/punkt.zip.

---------------------------------------------------------------------------
    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
---------------------------------------------------------------------------
Downloader> d

Download which package (l=list; x=cancel)?
  Identifier> stopwords
    Downloading package stopwords to /home/3/loua/nltk_data...
      Unzipping corpora/stopwords.zip.

---------------------------------------------------------------------------
    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
---------------------------------------------------------------------------
Downloader> d

Download which package (l=list; x=cancel)?
  Identifier> wordnet
    Downloading package wordnet to /home/3/loua/nltk_data...
      Unzipping corpora/wordnet.zip.

---------------------------------------------------------------------------
    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
---------------------------------------------------------------------------
Downloader> q
```

Next, ensure BeautifulSoup4 is installed:

```
> pip install beautifulsoup4
```

Lastly, ensure scikit-learn is installed:

```
> pip install scikit-learn
```

To run the code, first ensure the `lab4.py` file has execute privileges:

```
> chmod +x lab5.py
```

Next, ensure the `preprocessing/` and `minwisehash/` directories and their filetrees are correct with respect to `lab5.py` (based on the file tree in the overview). Also, ensure there is a `data/` directory in the same folder as `preprocessing.py` and the `data/` directory containing the `reut2-xxx.sgm` files is present. To begin preprocessing the data, run:

```
> python lab5.py
```

or

```
> ./lab5.py
```

The preprocessing and clustering might take some time to complete.

Once `preprocessing.py` finishes execution, two datasets files are generated (`dataset1.csv`, `dataset2.csv`) in the `/datasets` directory. To view these datasets, run:

```
> less datasets/datasetX.csv
```

where `X` is replaced with 1 or 2 depending on the dataset.

Once `clustering.py` finishes execution, the results of the 2x2 experiments will be outputted to the terminal.

## Development
* This module was developed using python 2.7.10 using the NLTK and BeautifulSoup4 modules.

### Adding More Feature Vectors
* Update the \_\_select\_features method in feature.py to extract a new list of feature vector & append to self.features 

### Adding More Clustering
* Add a new .py file to the clustering/algorithm directory
* Ensure this new clustering algorithm is a class with a construct and at least one method:
    * generate_clusters(training)
* Import the algorithm in clustering.py, add an instance of the algorithm to @clusterings, and the print strings

### Contributors
* Ankai Lou (lou.56@osu.edu)

## Change Log
2015-11-14 - Version 1.0.0:
* Initial code import
* Modified feature vector to be 0/1 instead of continuous
* Added functionality to compute baseline jaccard similarity
* Added functionality to generate randomized hash functions
* Added functionality to compute minwise hash sketch and signatures
* Added functionality to compute similarity of document signatures
* Added functionality to report runtime and accuracy of the code
* Basic code requirements fulfilled
* TODO: clean up code + make it faster & more modular
* TODO: write report in latex
