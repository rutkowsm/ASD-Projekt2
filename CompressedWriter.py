import Converter
import filereader
import HuffmanCodeBuilder

dictionary = HuffmanCodeBuilder.returnPath(HuffmanCodeBuilder.nodes[0])

srcText = filereader.reader()

converted = Converter.compressText(srcText, dictionary)

fname = "./Pliki/CompressedJabberwooky.txt"

newConverted = ''

i = 0
lenConverted = len(converted)
with open(fname, "w") as fout:
    while i < lenConverted:
        newConverted = newConverted + converted[i]
        i = i + 1
    fout.write(str(newConverted))
