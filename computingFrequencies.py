from numberToPattern import *
from patternToNumber import *

def computingFreqs(Text, k):
    textList = list(Text)
    frequencyArray = []
    for i in range(4**k-1+1):
        frequencyArray.insert(i, 0)
    #print frequencyArray
    for i in range(len(textList)-k+1):
        pattern = textList[i:i+k]
        j = patternToNumber(pattern)
        #print pattern, j, frequencyArray[j]
        #print frequencyArray
        x = frequencyArray[j] + 1
        #print x
        frequencyArray[j] += 1
    return frequencyArray

if __name__ == "__main__":
    Text = "ACGCGGCTCTGAAA"
    k = 2
    result = computingFreqs(Text, k)
    print result