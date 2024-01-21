# #lets do rsa 

import random 
import math

def _is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2  + 1):
        if number % i == 0:
            return False
    return True


def generate_prime(minvalue, maxvalue):
    prime = random.randint(minvalue, maxvalue)
    while not _is_prime(prime):
        prime = random.randint(minvalue, maxvalue)
    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d 
        
    raise ValueError("mod_inverse does not exist")

p,q = generate_prime(1000, 5000), generate_prime(1000, 5000)
while p == q:
    q = generate_prime(1000, 5000)

n = p*q 
phi = (p-1)*(q-1)
e = random.randint(3, phi)
while math.gcd(e, phi) != 1:
    e = random.randint(3, phi-1)

d = mod_inverse(e, phi)
print(f"public key is {e}")
print(f"private key is {d}")
print(f"phi of n is {phi}, keep it a secret tho ")
print(f"p is {p}")

message = "EVERYTHING IN ITS RIGHT PLACE"

message_encoded = [ord(c) for c in message]
# m ^ 3 mod n = c

ciphertext = [pow(c, e, n) for c in message_encoded]

# pow(c, e, n)

# c^e mod n 
print(ciphertext)
message_encoded = [pow(ch, d, n)for ch in ciphertext]
message = "".join(chr(ch) for ch in message_encoded)
print(message)
