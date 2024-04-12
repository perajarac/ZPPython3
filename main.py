from cesar import Cesar
from monoalpha import Monoalpha
from playfair import PlayFair

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

p = PlayFair(key=  'vetrobran')
p.encrypt(plain)
print(p)