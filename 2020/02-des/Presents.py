import numpy as np
import time

def PrimeTable(MaxLimit):
    AllNum = np.array(np.full(MaxLimit + 1, False))
    
    AllNum[2:3] = True
    AllNum[5::6] = True
    AllNum[7::6] = True      
    
    p = 6
    
    while p + 1 < MaxLimit:
        if AllNum[p-1]:
            for y in range((p-1)**2, len(AllNum), p-1):
                AllNum[y] = False

        if AllNum[p+1]:
            for z in range((p+1)**2, len(AllNum), p+1):
                AllNum[z] = False
        
        p += 6
    
    return AllNum


def PresentsToScrap(Top, AllNum):
    if AllNum[Top]:
        return Top
    
    for i in range(Top, 0, -1):
        if AllNum[i]:
            return i


def DeletingPresents(Limit):
    counter = i = 0

    primes = PrimeTable(Limit)
    
    while i <= Limit:
        if "7" in str(i):
            i += PresentsToScrap(i, primes) + 1
        else:
            counter += 1
            i += 1
                
    return counter


# =============================================================================
# Functions
# Execution
# =============================================================================

start = time.time()


PrimeTable(123456789)


print(f'Total tid: {time.time() - start} sek')



















