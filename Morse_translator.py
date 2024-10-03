class Morse:
    
    
    decode = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 
        'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 
        'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 
        'y': '-.--', 'z': '--..', ' ': ' '
    }
    def __init__(self, sequence):
        self.sequence = sequence

    def set(self, sequence):
        self.sequence = sequence
    
    def get(self):
        return self.sequence
    
    def only_small_letters(self):
        self.sequence = self.sequence.lower()
        print(self.sequence)
        return self.sequence
    
    def translate(self):
        self.only_small_letters()

        translated_sequence = []
        
        for char in self.sequence:
            if char in self.decode:
                translated_sequence.append(self.decode[char])
            else:
                translated_sequence.append('?')  # Znak nieznany
        
        morse_code = ' '.join(translated_sequence)

        # Wypisywanie przetłumaczonego kodu Morse'a
        print(morse_code)

        # Zwracanie przetłumaczonego kodu Morse'a
        return morse_code
if __name__ == "__main__":
    translator = Morse("AAA")
    translator.translate()  # Przetłumaczenie i wypisanie ciągu w kodzie Morse'a

# Ustawianie nowej sekwencji i tłumaczenie
    translator.set("LABY")
    translator.translate()  # Przetłumaczenie i wypisanie nowego ciągu