import pdb

def patternCount(Text, Pattern):
    count = 0
    textList = list(Text)
    patternList = list(Pattern)
    for i in range(0,len(textList)-len(patternList)+1,1):
        if textList[i:i+len(patternList)] == patternList:
            count += 1
    return count

if __name__ == "__main__":
    Text = "GCGCG"
    Pattern = "GCG"
    resultCount = patternCount(Text, Pattern)
    print resultCount