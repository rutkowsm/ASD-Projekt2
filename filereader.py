
from typing import final


try:
    def reader():
        fSrcName = "./Pliki/jaberwooky.txt"
        # Otwarcie pliku, wpisanie znaków do listy i zamknięcie
        fileSrc = open(fSrcName, "r")
        fileSrcText = fileSrc.read()
        fileSrc.close()
        return fileSrcText


except FileNotFoundError as error:
    print("File is not available:", type(error))
except Exception as error:
    print("Something went wrong:", type(error))
