import collections.Counter
def getUniqueWords(Tweet_input.txt):
    uniqueWords = Counter()

    for word in allWords:
        uniqueWords[word]+=1
    return uniqueWords.keys() 
