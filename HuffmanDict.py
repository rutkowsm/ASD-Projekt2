from operator import itemgetter
import filereader
# Liczenie znaków
# Definicja funkcji liczącej


def countCharacters(text):

    textList = list(text)
    charCount = len(textList)

    # Deduplikacja listy i liczba unikalnych znaków
    uniqueChars = list(dict.fromkeys(textList))
    uniqueCharCount = len(uniqueChars)

    # tablice częstości wystąpień i ostateczna puste
    freqTable = []
    finalTable = []

    # Uzupełnianie tablicy częstości wystąpień zerami,
    i = 0
    while i < uniqueCharCount:
        freqTable.append(0)
        i = i + 1

    # Zliczanie poszczególnych znaków

    i = 0
    while i < charCount:
        j = uniqueChars.index(textList[i])
        freqTable[j] = freqTable[j] + 1
        i = i + 1

    # scalenie obu tablic w jedną ostateczną słoownikową złożoną z tablic dwuelementowych
    # ([{'char': znak, 'freq': l. wystąpień}])

    x = 0
    while x < uniqueCharCount:
        finalTable.append({'char': uniqueChars[x], 'freq': freqTable[x]})
        x = x + 1

    return finalTable

    ###########################
    # Testing block
    # x = 15

    # if freqTable[x] == text.count(uniqueChars[x]):
    #     print("Result is the same!")
    # else:
    #     print("Results do not match!")
    ###########################

# Definicja funkcji budującej drzewo binarne znaków danego tekstu


def huffmanTree(text):
    charCount = countCharacters(text)

    charCountSorted = sorted(charCount, key=itemgetter('freq'))
    print(charCountSorted)


huffmanTree(filereader.reader())
