
def reverseComplement(Text):
    count = 0
    textList = list(Text)
    result = []
    for i in range(0,len(textList)):
        if textList[i] == "A":
            result.insert(0,"T")
        elif textList[i] == "T":
            result.insert(0,"A")
        elif textList[i] == "G":
            result.insert(0,"C")
        elif textList[i] == "C":
            result.insert(0,"G")
    return "".join(result)

def readData(filename):
    with open(filename, 'r') as f:
        f.readline() # Skip input line
        Input = f.readline()
        f.readline()
        Output = f.readline()
        return Input.strip(), Output.strip()

if __name__ == "__main__":
    Input, Output = readData('reverse_complement_data.txt')
    #Text, k = readData('dataset_2_9.txt')
    #Text = "AAAACCCGGT"
    result = reverseComplement(Input)
    print result
    print Output
    assert(result == Output)