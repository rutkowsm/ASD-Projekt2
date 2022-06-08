import Sorter
import filereader
import NodeClass
import HeapSort

text = filereader.reader()
sortedFreq = Sorter.sortFreqArray(text)

node = NodeClass.node

binDictList = []


def returnPath(node, travers=''):
    newTravers = travers + str(node.travers)

    if(node.left):
        returnPath(node.left, newTravers)

    if(node.right):
        returnPath(node.right, newTravers)

    if(not node.left and not node.right):
        dictElement = [node.char, newTravers]
        binDictList.append(dictElement)
    return binDictList


nodes = []

for x in range(len(sortedFreq)):
    nodes.append(node(sortedFreq[x][0], sortedFreq[x][1]))


while len(nodes) > 1:

    # pick 2 smallest nodes
    left = nodes[0]
    right = nodes[1]

    # assign directional value to these nodes
    left.travers = 0
    right.travers = 1

    # combine the 2 smallest nodes to create
    # new node as their parent
    newChar = left.char+right.char
    newFreq = left.freq+right.freq
    newNode = node(newChar, newFreq, left, right)
    HeapSort.heapSortNd(nodes)

    # remove the 2 nodes and add their
    # parent as new node among others
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)


# print(returnPath(nodes[0]))
# print(sortedFreq)
