from numberToPattern import numberToPattern
from patternToNumber import patternToNumber, symbolToNumber

def computingFreqs(Text, k):
    textList = list(Text)
    frequencyArray = []
    for i in range(4**k-1+1):
        frequencyArray.insert(i, 0)
    for i in range(len(textList)-k+1):
        pattern = textList[i:i+k]
        j = patternToNumber(pattern)
        x = frequencyArray[j] + 1
        frequencyArray[j] += 1
    return frequencyArray

def read_data(filename):
    with open(filename, 'r') as f:
        Text = f.readline()
        k = f.readline()
        return Text.strip(), int(k)

if __name__ == "__main__":
    Text, k = read_data('dataset_2994_5.txt')
    result = computingFreqs(Text, k)
    out = []
    for i in result:
        out.append(str(i))
    print " ".join(out)