def _checkforprime(number):
    if number<2:
        return False
    for i in range(2, number//2 +1):
        if number%i == 0:
            return False
    return True
