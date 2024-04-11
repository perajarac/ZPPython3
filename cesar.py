class Cesar:

    def __init__(self,shift):
        self.shift = shift
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.shifted_alphabet = self.shift_alphabet(self.alphabet, shift)

    def shift_alphabet(self, alphabet, shift):
        shifted_alphabet = ''
        for char in alphabet:
            new_pos = (ord(char)-ord('a') + shift) % 26

            new_char = chr(new_pos + ord('a'))
            shifted_alphabet += new_char

        return shifted_alphabet
    
    def encrypt(self, message):
        ret = ''
        for char in message:
            if(char == ' '):
                ret += ' '
                continue
            indexa = self.alphabet.index(char)
            ret += self.shifted_alphabet[indexa]

        return ret
    
    def decrypt(self, cypher):
        ret = ''
        for char in cypher:
            if(char == ' '):
                ret += ' '
                continue
            indexs = self.shifted_alphabet.index(char)
            ret += self.alphabet[indexs]

        return ret