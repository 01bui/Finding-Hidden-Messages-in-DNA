def hamDistance(str1, str2):
    diff = 0
    for char1, char2 in zip(str1, str2):
            if char1 != char2:
                    diff += 1
    return diff

if __name__ == "__main__":
    result = hamDistance("GGGCCGTTGGT", "GGACCGTTGAC")
    print result