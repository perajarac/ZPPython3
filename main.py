from cesar import Cesar
from monoalpha import Monoalpha

plain = 'napadamo u podne ako ne bude vetra'

print('Cesar testing crypting and decrypting \n')
c = Cesar(shift = 3)
cypher_cesar = c.encrypt(plain)
c.decrypt()
print(c)

m = Monoalpha(key = 'qwertzuiopasdfghjklyxcvbnm')
m.encrypt(plain)
m.decrypt()
print(m)