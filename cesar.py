class Cesar:

    def __init__(self,shift):
        self.shift = shift
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.shifted_alphabet = self.shift_alphabet(self.alphabet, shift)
        self.cypher = ''
        self.plain = ''

    def shift_alphabet(self, alphabet, shift):
        shifted_alphabet = ''
        for char in alphabet:
            new_pos = (ord(char)-ord('a') + shift) % 26

            new_char = chr(new_pos + ord('a')) #na ovo mesto tekuceg dolazi onaj koji je shift mesta ispred njega
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
        self.cypher = ret
        return ret
    
    def decrypt(self):
        ret = ''
        for char in self.cypher:
            if(char == ' '):
                ret += ' '
                continue
            indexs = self.shifted_alphabet.index(char)
            ret += self.alphabet[indexs]
        self.plain = ret
        return ret
    
    def __str__(self):     
        return  'Cesar testing crypting and decrypting \n'+'Encrypted text: ' + self.cypher+ '\nDecrypted text: ' + self.plain+'\n------------------------------------------\n'