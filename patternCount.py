import pdb

def patternCount(Text, Pattern):
    count = 0
    textList = list(Text)
    patternList = list(Pattern)
    print len(textList)
    print len(patternList)
    for i in range(0,len(textList)-len(patternList)+1,1):
        if textList[i:i+len(patternList)] == patternList:
            count += 1
    return count

def readData(filename):
    with open(filename, 'r') as f:
        f.readline() # Skip input line
        Text = f.readline()
        Pattern = f.readline()
        return Text.strip(), Pattern.strip()

if __name__ == "__main__":
    Text, Pattern = readData('PatternCount.txt')
    resultCount = patternCount(Text, Pattern)
    print resultCount