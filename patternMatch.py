import pdb

def patternMatch(Text, Pattern):
    pos =[]
    textList = list(Text)
    patternList = list(Pattern)
    for i in range(0,len(textList)):
        if textList[i:i+len(patternList)] == patternList:
            pos.append(str(i))
    return " ".join(pos)

def readData(filename):
    with open(filename, 'r') as f:
        #f.readline() # Skip input line
        #Pattern = f.readline()
        Text = f.readline()
        #f.readline() # Skip
        #Output = f.readline()
        return Text.strip()

if __name__ == "__main__":
    Text = readData('Vibrio_cholerae.txt')
    #Text, Pattern = readData('dataset_3_5.txt')
    #print Text
    #print Pattern
    #Text, Pattern, Output = readData('pattern_matching_data.txt')
    #Pattern = "ATAT"
    #Text = "GATATATGCATATACTT"
    result = patternMatch(Text, "CTTGATCAT")
    print result
    #print Output
    #assert(result == Output)