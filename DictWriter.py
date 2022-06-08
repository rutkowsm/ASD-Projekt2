import filereader
import HuffmanCodeBuilder


fname = "./Pliki/dict.txt"

with open(fname, "w") as fout:
    fout.write(str(HuffmanCodeBuilder.returnPath(HuffmanCodeBuilder.nodes[0])))
