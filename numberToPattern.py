import pdb

def numberToSymbol(number):
    if number == 0:
        symbol = "A"
    elif number == 1:
        symbol = "C"
    elif number == 2:
        symbol = "G"
    elif number == 3:
        symbol = "T"
    return symbol

def numberToPattern(index,k):
    if k == 1:
        return numberToSymbol(index)
    prefixIndex = index/4
    r = index % 4
    print index, 4, prefixIndex, r
    symbol = numberToSymbol(r)
    prefixPattern = numberToPattern(prefixIndex,k-1)
    return prefixPattern + symbol

if __name__ == "__main__":
    index = 45
    k = 4
    result = numberToPattern(index,k)
    print result