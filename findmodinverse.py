#for finding d 
def _findingmodinverse(e, phi):
    for d in range(3, phi):
        if (d*e) % phi == 1:
            return d
    
    raise ValueError("NAH ID MODINVERSE")
