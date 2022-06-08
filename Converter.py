import filereader
import HuffmanCodeBuilder

dictionary = HuffmanCodeBuilder.returnPath(HuffmanCodeBuilder.nodes[0])

print(dictionary)

srcText = filereader.reader()


def compressText(text, dict):
    textList = list(text)

    lenTextList = len(textList)
    lenDictionary = len(dictionary)
    i = 0
    while i < lenTextList:
        j = 0
        while j < lenDictionary:
            if textList[i] == dictionary[j][0]:
                textList[i] = dictionary[j][1]
            j = j + 1
        i = i + 1

    return textList

# print(compressText(srcText, dictionary))
