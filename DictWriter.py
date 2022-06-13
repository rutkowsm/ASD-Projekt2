import filereader
import HuffmanCodeBuilder


fname = "./Pliki/CompressedJaberwooky.txt"

with open(fname, "w") as fout:
    fout.write(str(HuffmanCodeBuilder.returnPath(HuffmanCodeBuilder.nodes[0])))
