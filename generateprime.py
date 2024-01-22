import random
from checkprime import _checkforprime
def _generateprimenumbers(minvalue, maxvalue):
    primenumber = random.randint(minvalue, maxvalue)
    while not _checkforprime(primenumber):
        primenumber = random.randint(minvalue , maxvalue)
    return primenumber
