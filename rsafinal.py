import random 
import math 
from Crypto.Util.number import inverse
from codecs import decode
def _checkforprime(number):
    if number<2:
        return False
    for i in range(2, number//2 +1):
        if number%i == 0:
            return False
    return True

def _generateprimenumbers(minvalue, maxvalue):
    primenumber = random.randint(minvalue, maxvalue)
    while not _checkforprime(primenumber):
        primenumber = random.randint(minvalue , maxvalue)
    return primenumber

#for finding d 
def _findingmodinverse(e, phi):
    for d in range(3, phi):
        if (d*e) % phi == 1:
            return d
    
    raise ValueError("NAH ID MODINVERSE")

p, q = _generateprimenumbers(1000, 5000), _generateprimenumbers(10000, 50000)

while p == q:
    p = _generateprimenumbers(1000, 5000)

n = p*q 

phiofn = (p-1)*(q-1)

e = random.randint(3, phiofn-1)
while math.gcd(e,phiofn) != 1:
    e = random.randint(3, phiofn)

d = _findingmodinverse(e, phiofn)

print(f"GENERAL INFORMATION: \n{e} is the public key\n{d} is the private key\n{p,q}are the two prime numbers")


message = "EVERYTHING IN ITS RIGHT PLACE"

#just encoded not encrypted

messageencoded=[ord(c) for c in message]
# print(messageencoded)

# c = m^d mod n
ciphertext = [pow(ch,e,n) for ch in messageencoded]

#print(ciphertext)

#decrypt

messageencoded = [pow(ch, d, n) for ch in ciphertext]
#print(messageencoded)
# message = "".join(chr(ch) for ch in messageencoded)

for x in messageencoded:
    y = chr(x)
    print(y, end="")
    
'''TESTING RSA ON A COMPETITIVE EVENT QUESTION --> BOOT2ROOT CTF(CAPTURE THE FLAG 2018'''

# n=71641831546926719303369645296528546480083425905458247405279061196214424558100678947996271179659761521775290973790597533683668081173314940392098256721488468660504161994357

# e = 65537


# c=63127079832500412362950100242549738176318170072331491750802716138621322974529994914407846448954487685068331564008936808539420562251661435790855422130443584773306161128156

# #solution 
# #step 1 --> finding the two prime numbers from which is is made

# p = 8464149782874043593254414191179506861158311266932799636000173971661904149225893113311

# q = 8464149782874043593254414191179506861158311266932799636000173971661904149225893113387

# phi_n = (p-1)*(q-1)
# #here we used inverse function from the crypto util library, but out inverse function can also be used but has a slow output processing speed
# d = inverse(e, phi_n)

# m = pow(c, d, n)
# print (decode(hex(m)[2:],'hex'))

#caesars encryption 


import string

plaintext = input("Enter what you want to reverse/decrypt: ")
userchoice = int(input("Enter 1 for encrypting and 2 for decrypting: "))

def encryptDawords(plaintext):
    shift = int(input("Enter the degree of shift you want [1 = 1 shift of each letter]: "))
    if shift > 26:
        shift = shift % 26

    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    tableforencrypt = str.maketrans(alphabet, shifted)

    encrypted = plaintext.translate(tableforencrypt)
    return encrypted

def decryptDawords(plaintext):
    shift = int(input("Enter the degree of shift you performed previously: "))
    shift2 = 26 - shift

    alphabet = string.ascii_lowercase
    shifted = alphabet[shift2:] + alphabet[:shift2]
    tableforreverse = str.maketrans(alphabet, shifted)

    decrypted = plaintext.translate(tableforreverse)
    return decrypted

if userchoice == 1:
    encrypted_text = encryptDawords(plaintext)
    print("Encrypted text:", encrypted_text)

elif userchoice == 2:
    decrypted_text = decryptDawords(plaintext)
    print("Decrypted text:", decrypted_text)

else:
    raise ValueError("Choice is not applicable")

