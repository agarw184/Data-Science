from helper import plotHisto
import operator

hw8_1 =__import__("hw8-1")
helper =__import__("helper")

englishfreqlist = []
frenchfreqlist = []
germanfreqlist = []
italianfreqlist = []
portuguesefreqlist =[]
spanishfreqlist = []
mysteryfreqlist = []

# 6 dictionaries
dictionary_final1 = hw8_1.getDict('ngrams/english.txt')
dictionary_final2 = hw8_1.getDict('ngrams/french.txt')
dictionary_final3 = hw8_1.getDict('ngrams/german.txt')
dictionary_final4 = hw8_1.getDict('ngrams/italian.txt')
dictionary_final5 = hw8_1.getDict('ngrams/portuguese.txt')
dictionary_final6 = hw8_1.getDict('ngrams/spanish.txt')
dictionary_final7 = hw8_1.getDict('ngrams/mystery.txt')

languagesorted = {}
languagesorted.update(dictionary_final1)
languagesorted.update(dictionary_final2)
languagesorted.update(dictionary_final3)
languagesorted.update(dictionary_final4)
languagesorted.update(dictionary_final5)
languagesorted.update(dictionary_final6)


#Converting all to dictionaries
languagesorted = sorted(languagesorted.items(), key = lambda x: x[0])
languagesorted = dict(languagesorted)

for word in languagesorted:
    if word in dictionary_final1:
        englishfreqlist.append(dictionary_final1[word])
    else:
        englishfreqlist.append(0)

for word in languagesorted:
    if word in dictionary_final2:
        frenchfreqlist.append(dictionary_final2[word])
    else:
        frenchfreqlist.append(0)

for word in languagesorted:
    if word in dictionary_final3:
        germanfreqlist.append(dictionary_final3[word])
    else:
        germanfreqlist.append(0)

for word in languagesorted:
    if word in dictionary_final4:
        italianfreqlist.append(dictionary_final4[word])
    else:
        italianfreqlist.append(0)

for word in languagesorted:
    if word in dictionary_final5:
        portuguesefreqlist.append(dictionary_final5[word])
    else:
        portuguesefreqlist.append(0)

for word in languagesorted:
    if word in dictionary_final6:
        spanishfreqlist.append(dictionary_final6[word])
    else:
        spanishfreqlist.append(0)

for word in languagesorted:
    if word in dictionary_final7:
        mysteryfreqlist.append(dictionary_final7[word])
    else:
        mysteryfreqlist.append(0)

plotHisto(englishfreqlist,'english.png',)
plotHisto(frenchfreqlist,'french.png')
plotHisto(germanfreqlist,'german.png')
plotHisto(italianfreqlist,'italian.png')
plotHisto(portuguesefreqlist,'portuguese.png')
plotHisto(spanishfreqlist,'spanish.png')
plotHisto(mysteryfreqlist,'mystery.png')
