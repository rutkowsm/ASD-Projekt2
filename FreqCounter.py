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
        finalTable.append([uniqueChars[x], freqTable[x]])
        x = x + 1

    return finalTable


def listOfChar(text):
    charCount = countCharacters(text)

    i = 0
    charList = []
    while i < len(charCount):
        charList.append(charCount[i][0])
        i = i + 1

    return charList


def listOfFreq(text):
    charCount = countCharacters(text)

    i = 0
    freqList = []
    while i < len(charCount):
        freqList.append(charCount[i][1])
        i = i + 1

    return freqList
