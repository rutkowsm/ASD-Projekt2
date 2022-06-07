from operator import itemgetter
import filereader

# A Huffman Tree Node


class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # symbol name (character)
        self.symbol = symbol

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # tree direction (0/1)
        self.huff = ''


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


# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree


def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)

    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)

        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")

# text to check


text = filereader.reader()

# characters for huffman tree
chars = listOfChar(text)
print(chars)

# frequency of characters
freq = listOfFreq(text)
print(freq)
# list containing unused nodes
nodes = []

# converting characters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))

while len(nodes) > 1:
    # sort all the nodes in ascending order
    # based on theri frequency
    nodes = sorted(nodes, key=lambda x: x.freq)

    # pick 2 smallest nodes
    left = nodes[0]
    right = nodes[1]

    # assign directional value to these nodes
    left.huff = 0
    right.huff = 1

    # combine the 2 smallest nodes to create
    # new node as their parent
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

    # remove the 2 nodes and add their
    # parent as new node among others
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

# Huffman Tree is ready!
printNodes(nodes[0])

# Liczenie znaków
# Definicja funkcji liczącej
