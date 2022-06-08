class node:
    def __init__(self, char, freq, left=None, right=None):

        # Znak
        self.char = char

        # Częstość wystąpień
        self.freq = freq

        # Gałąź lewa drzewa
        self.left = left

        # Gałąź prawa drzewa
        self.right = right

        # Lewy czy prawy - kopiec
        self.travers = ''
