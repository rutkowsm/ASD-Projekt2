from operator import itemgetter
import Sorter
import filereader

text = filereader()
sortedFreq = Sorter.sortFreqArray(text)

# A Huffman Tree Node


class node:
    def __init__(self, freq, char, left=None, right=None):
        # Częstość wystąpień
        self.freq = freq

        # Znak
        self.char = char

        # Gałąź lewa drzewa
        self.left = left

        # Gałąź prawa drzewa
        self.right = right

        # Lewy czy prawy - kopiec
        self.bin = ''


# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree

# def returnNodes(node, val=''):
#     # dodawanie wartości binarnych po drzewie
#     newVal = val + str(node.bin)

#     # zejście po drzewie w dół
#     if node.left:
#         return (node.left, newVal)
#     if node.right:
#         return (node.right, newVal)

#     # elementy końcowe (bez dzieci - bez gałęzi w lewo/prawo)
#     if not node.left and not node.right:
#         return (f"{node.char} -> {newVal}")

def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.bin)

    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)

        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        print(f"{node.char} -> {newVal}")


# list containing unused nodes
nodes = []

# converting characters and frequencies
# into huffman tree nodes
for x in range(len(sortedFreq)):
    nodes.append(node(sortedFreq[x][0], sortedFreq[x][1]))

while len(nodes) > 1:
    # sort all the nodes in ascending order
    # based on theri frequency
    nodes = sorted(nodes, key=lambda x: x.freq)

    # pick 2 smallest nodes
    left = nodes[0]
    right = nodes[1]

    # assign directional value to these nodes
    left.bin = 0
    right.bin = 1

    # combine the 2 smallest nodes to create
    # new node as their parent
    newNode = node(left.freq+right.freq, left.char+right.char, left, right)

    # remove the 2 nodes and add their
    # parent as new node among others
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

# Huffman Tree is ready!
printNodes(nodes[0])
