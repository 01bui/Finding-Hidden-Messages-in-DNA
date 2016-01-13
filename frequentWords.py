import pdb

def frequentWords(Text, k):

    frequentPatterns = []
    textList = list(Text)
    Count = []
    for i in range(len(textList)-k+1):
        Pattern = Text[i:i+k]
        Count.insert(i,patternCount(Text, Pattern))
        #print Pattern, Count
    maxCount = max(Count)

    for i in range(len(textList)-k+1):
        if Count[i] == maxCount:
            frequentPatterns.append(Text[i:i+k])
    return set(frequentPatterns)

def patternCount(Text, Pattern):
    count = 0
    textList = list(Text)
    patternList = list(Pattern)
    for i in range(0,len(textList)-len(patternList)+1,1):
        if textList[i:i+len(patternList)] == patternList:
            count += 1
    return count

def readData(filename):
    with open(filename, 'r') as f:
        #f.readline() # Skip input line
        Text = f.readline()
        Pattern = f.readline()
        return Text.strip(), Pattern.strip()

if __name__ == "__main__":
    #Text, k = readData('dataset_2_6.txt')
    Text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4
    result = frequentWords(Text, k)
    print result