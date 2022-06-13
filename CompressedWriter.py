import Converter
import filereader
import HuffmanCodeBuilder

dictionary = HuffmanCodeBuilder.returnPath(HuffmanCodeBuilder.nodes[0])

srcText = filereader.reader()

converted = Converter.compressText(srcText, dictionary)

fname = "./Pliki/CompressedJaberwooky.txt"

newConverted = ''

i = 0
lenConverted = len(converted)
with open(fname, "a") as fout:
    fout.write(str('\n'))
    while i < lenConverted:
        newConverted = newConverted + converted[i]
        i = i + 1
    fout.write(str(newConverted))
