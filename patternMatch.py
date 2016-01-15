import pdb

def patternMatch(Text, Pattern):
    pos =[]
    textList = list(Text)
    patternList = list(Pattern)
    for i in range(0,len(textList)):
        if textList[i:i+len(patternList)] == patternList:
            pos.append(i)
    return pos

def readData(filename):
    with open(filename, 'r') as f:
        #f.readline() # Skip input line
        Text = f.readline()
        Pattern = f.readline()
        return Text.strip(), Pattern.strip()

if __name__ == "__main__":
    #Text, Pattern = readData('dataset_2_6.txt')
    Pattern = "ATAT"
    Text = "GATATATGCATATACTT"
    result = patternMatch(Text, Pattern)
    print result