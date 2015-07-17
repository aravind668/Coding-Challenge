import collections.Counter
def getUniqueWords(allWords):
    uniqueWords = Counter()

    for word in allWords:
        uniqueWords[word]+=1
    return uniqueWords.keys() 
