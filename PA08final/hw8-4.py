import helper
from helper import remove_punc
import nltk
nltk.download("punkt")
nltk.download("wordnet")
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np
import math as m


#Clean and lemmatize the contents of a document
#Takes in a file name to read in and clean
#Return a list of words, without stopwords and punctuation, and with all words lemmatized
# NOTE: Do not append any directory names to doc -- assume we will give you
# a string representing a file name that will open correctly
def readAndCleanDoc(doc) :
    #1. Open document, read text into *single* string
    myfile = open(doc, 'r')
    tmp = myfile.read()

    #2. Tokenize string using nltk.tokenize.word_tokenize
    tokens = word_tokenize(tmp)

    #3. Filter out punctuation from list of words (use remove_punc)
    tokens = remove_punc(tokens)

    #4. Make the words lower case
    tokens = [word.lower() for word in tokens]

    #5. Filter out stopwords
    stop = stopwords.words('english')
    tokens_clean = [x for x in tokens if not x in stop]

    #6. Lemmatize words
    lemmatizer = WordNetLemmatizer()
    tokens_clean_lem = [lemmatizer.lemmatize(word) for word in tokens_clean]
    words = tokens_clean_lem

    return words
#Builds a doc-word matrix for a set of documents
#Takes in a *list of filenames*
#
#Returns 1) a doc-word matrix for the cleaned documents
#This should be a 2-dimensional numpy array, with one row per document and one
#column per word (there should be as many columns as unique words that appear
#across *all* documents
#
#Also returns 2) a list of words that should correspond to the columns in
#docword
def buildDocWordMatrix(doclist) :
    #1. Create word lists for each cleaned doc (use readAndCleanDoc)
    #2. Use these word lists to build the doc word matrix
    word_vec = []
    docword = []
    wordlist = []
    for doc in doclist:
        listobt = readAndCleanDoc(doc)
        for word in listobt:
            if(not(word in word_vec)):
                word_vec.append(word)
    word_vec.sort()
    wordlist = word_vec
    doc_word = []

    for doc in doclist:
        listobt = readAndCleanDoc(doc)
        doc_vec = [0.0]*len(word_vec)
        for word in listobt:
            if word in word_vec:
                ind = word_vec.index(word)
                doc_vec[ind] += 1.0
        doc_word.append(doc_vec)
    doc_word.sort()
    docword = doc_word
    docword = np.array(docword)
    return docword, wordlist

#Builds a term-frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns a term-frequency matrix, which should be a 2-dimensional numpy array
#with the same shape as docword
def buildTFMatrix(docword):
#fill in
    for i,row in enumerate(docword):
        totalsum = sum(row)
        for col,curele in enumerate(row):
            docword[i][col] = (curele / totalsum)
    tf = docword
    return tf

#Builds an inverse document frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns an inverse document frequency matrix (should be a 1xW numpy array where
#W is the number of words in the doc word matrix)
#Don't forget the log factor!
def buildIDFMatrix(docword):
    #fill in
    idfinitial = []
    idf = []
    for i in docword.T:
        colsum = 0
        for j in i:
            if (j != 0):
                colsum = colsum + 1
        divval = m.log(((len(docword))/colsum),10)
        idfinitial.append(divval)
    idf.append(idfinitial)
    idf = np.array(idf)
    return idf

#Builds a tf-idf matrix given a doc word matrix
def buildTFIDFMatrix(docword) :

    #fill in
    tfidf = []
    tf = buildTFMatrix(docword)
    idf = buildIDFMatrix(docword)
    for i in tf:
        for j in idf:
            val = i * j
            tfidf.append(val)
    tfidf = np.array(tfidf)
    return tfidf

#Find the three most distinctive words, according to TFIDF, in each document
#Input: a docword matrix, a wordlist (corresponding to columns) and a doclist
# (corresponding to rows)
#Output: a dictionary, mapping each document name from doclist to an (ordered
# list of the three most common words in each document

#fill in
#you might find numpy.argsort helpful for solving this problem:
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html
def findDistinctiveWords(docword, wordlist, doclist) :
    distinctiveWords = {}
    wordcompute = {}
    listfinal = []
    wordlistfinal = []
    wordcomputelist = []
    tfidf = buildTFIDFMatrix(docword)

    for i in range (len(tfidf)):
        listfinal = list(np.argsort(-tfidf[i])[0:3])
        wordlistfinal.append(listfinal)

    for i in range (len(wordlistfinal)):
        val = wordlistfinal[i]
        wordcomputelist = []
        for value in val:
            wordcomputelist.append(wordlist[value])
            distinctiveWords[doclist[i]] = wordcomputelist
    return distinctiveWords
