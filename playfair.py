class PlayFair:
    def __init__(self,key):
        self.matrix = [[[] for _ in range(5)] for _ in range(5)]
        self.key = key.replace(' ', '')
        self.key = self.remove_duplicates(self.key)
        self.initialize_matrix()
        self.plain = []
        self.cypher = ''

    def remove_duplicates(self, word):
        seen = set()
        result = []
        
        for letter in word:
            if letter not in seen:
                seen.add(letter)
                result.append(letter)
        
        return ''.join(result)

    def initialize_matrix(self):
        working_string = self.key
        temp_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)] #generating alphabet
        temp_alphabet.remove("j")
        for i in range(5):
            for j in range(5):
                if(i*5 + j<len(working_string)):
                    self.matrix[i][j] = working_string[i*5+j]
                    temp_alphabet = [letter for letter in temp_alphabet if letter!=working_string[i*5+j]]
                else:
                    self.matrix[i][j] = temp_alphabet[0]
                    temp_alphabet.pop(0)

    def modify_plain(self, text):
        modified = []
        for i in range(len(text)-1):
            if(text[i] == ' '):
                continue
            modified.append(text[i])
            if(text[i] == text[i+1]):
                modified.append('x')
        
        modified.append(text[-1])
        if(len(modified)%2 == 1):
            modified.append('x')

        temp = []
        for i in range(len(modified)):
            if(i%2 == 1 and i!=0):
                curr = modified[i-1] + modified[i]
                temp.append(curr)

        
        return temp
    
    def find_el(self,letter):
        for i in range(5):
            for j in range(5):
                if(self.matrix[i][j] == letter):
                    return (i,j)
        return None
                
    def crypt(self, plain):
        self.plain = self.modify_plain(plain)
        for el in self.plain:
            fi_fj = self.find_el(el[0])
            if fi_fj is not None:
                fi,fj = fi_fj
            si_sj = self.find_el(el[1])
            if si_sj is not None:
                si,sj = si_sj
            if(fi == si): #isti red
                if(fj + 1 < 5):
                    self.cypher += self.matrix[fi][fj+1]
                elif(fj + 1 == 5):
                    self.cypher += self.matrix[fi][0]           
                if(sj + 1 < 5):
                    self.cypher += self.matrix[si][sj+1]
                elif(sj + 1 == 5):
                    self.cypher += self.matrix[si][0]
            elif(fj == sj):
                if(fi + 1 < 5):
                    self.cypher += self.matrix[fi+1][fj]
                elif(fi + 1 == 5):
                    self.cypher += self.matrix[0][fj]           
                if(si + 1 < 5):
                    self.cypher += self.matrix[si+1][sj]
                elif(si + 1 == 5):
                    self.cypher += self.matrix[0][sj]
            else:
                self.cypher += self.matrix[fi][sj]
                self.cypher += self.matrix[si][fj]
            
            self.cypher += ' '

    def __str__(self):     
        return  'Playfair testing crypting and decrypting \n'+'Encrypted text: ' + self.cypher+ '\nDecrypted text: ' + ''.join(self.plain)+'\n------------------------------------------\n'