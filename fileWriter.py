import filereader
import HuffmanList


fname = "./Pliki/dict.txt"

with open(fname, "w") as fout:
    fout.write(HuffmanList.returnNodes(str(HuffmanList.nodes[0])))
