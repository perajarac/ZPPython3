from cesar import Cesar

c = Cesar(shift = 3)

plain = 'napadamo u podne ako ne bude vetra'

cypher = c.encrypt(plain)
print(c.decrypt(cypher))