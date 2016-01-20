from numberToPattern import numberToPattern
from computingFrequencies import computingFreqs

def computingFreqs(Text, k):
    frequentPatterns = []
    frequencyArray = computingFreqs(Text,k)
    maxCount = max(frequencyArray)
    for i in range(4**k-1+1):
        if frequencyArray[i] == maxCount:
            pattern = numberToPattern(i,k)
            frequentPatterns.append(pattern)
    return frequentPatterns

if __name__ == "__main__":
    Text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4
    result = computingFreqs(Text, k)
    print result