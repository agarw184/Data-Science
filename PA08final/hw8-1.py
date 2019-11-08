#Arguments:
#  filename: name of file to read in
#Returns: a list of strings, each string is one line in the file
#hints: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#       https://docs.python.org/3/library/stdtypes.html#str.splitlines
def getText(filename) :
    #fill in
    textlist = []
    currentline = 0
    infptr = open(filename, 'r')
    currentline = infptr.read()
    textlist = currentline.splitlines()
    infptr.close()
    return textlist
#Arguments:
#  line: a string of text
#Returns: a list of n-grams
#Notes: make sure to pad the beginning and end of the string with '_'
#       make sure to convert the string to lower-case
#       so "Hello" should be turned into "__hello__" before processing
def getNgrams(line):
    #fill in
    ngramlist = []
    newlowercasestring = line.lower()
    newlowercasestring = newlowercasestring.strip('\n')
    newlowercasestring = '__' + newlowercasestring + '__'
    for i in range (len(newlowercasestring)-2):
        ngramlist.append(newlowercasestring[i:i+3])
    return ngramlist

#Arguments:
#  filename: the filename to create an n-gram dictionary for
#Returns: a dictionary, with ngrams as keys, and frequency of that ngram as the value.
#Notes: Remember that getText gives you a list of lines, and you want the ngrams from
#       all the lines put together.
#       use 'map', use getText, and use getNgrams
#Hint: dict.fromkeys(l, 0) will initialize a dictionary with the keys in list l and an
#      initial value of 0
def getDict(filename):

    ##data structures
    listwithline = []
    gramslist = []
    newgramslist = []
    dictionary = {}
    ##counters
    i = 0
    j = 0
    k = 0
    listwithline = getText(filename)
    for i in range (len(listwithline)):
        gramslist += getNgrams(listwithline[i])
    dictionary = dict.fromkeys(gramslist,0)
    for gram in (gramslist):
        dictionary[gram] += 1
    #print(dictionary)
    return dictionary
