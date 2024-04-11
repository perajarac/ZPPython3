class Monoalpha:

    def __init__(self, key):
        self.key = key
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.cypher = ''
        self.plain = ''
    
    def encrypt(self, plain):
        ret = ''
        for char in plain:
            if(char == ' '):
                ret += ' '
                continue
            indexa = self.alphabet.index(char)
            ret += self.key[indexa]
        self.cypher = ret
        return ret
    
    def decrypt(self):
        ret = ''
        for char in self.cypher:
            if(char == ' '):
                ret += ' '
                continue
            indexc = self.key.index(char)
            ret += self.alphabet[indexc]
        self.plain = ret
        return ret
    
    def __str__(self):     
        return  'Monoalphabet testing crypting and decrypting \n'+'Encrypted text: ' + self.cypher+ '\nDecrypted text: ' + self.plain+'\n------------------------------------------\n'