
'''
Created on 12 Dec 2019

@author: williamrosenberg and jesperbrodin
'''

import hashlib
from math import ceil
import random


hLen = 20
k = 128


def I20SP (x, xLen):
    if x >= 256**xLen:
        return "integer too large"
    return (hex(x)[2:].zfill(2*xLen))



def MGF1(mgfSeed, maskLen):
    if maskLen >= 2**32 * hLen:
        return "mask too long"
    T = ""
    for i in range(0, int(ceil(maskLen / hLen))):
        C = I20SP (i, 4)
        T = T + hashlib.sha1(bytearray.fromhex(mgfSeed + C)).hexdigest()
                
    return T[:2*maskLen]


def OAEP_encode(M, seed):
    if len(M) > (k - 2 * hLen - 2):
        return "message too long"
    L = ""
    lHash = hashlib.sha1(bytearray(L.encode())).hexdigest()
    PS = "".zfill(((k - int(len(M)/2) - 2*hLen) - 2)*2)
    DB = lHash + PS + "01" + M 
    random_octet = str(bytearray(random.getrandbits(8) for _ in range(hLen)))
    dbMask = MGF1(seed, k - hLen - 1)
    maskedDB = hex(int(DB, 16) ^ int(dbMask, 16))[2:]
    seedMask = MGF1(maskedDB, hLen)
    maskedSeed = hex(int(seed, 16) ^ int(seedMask, 16))[2:]
    EM = "00" + maskedSeed + maskedDB
    return EM

def OAEP_decode (EM):
    L = ""
    lHash = hashlib.sha1(bytearray(L.encode())).hexdigest()
   
    Y = EM[:2]
    maskedSeed = EM[2:2 * hLen + 2]
    maskedDB = EM[2 * hLen + 2:]
    seedMask = MGF1(maskedDB, hLen)
   
    seed = hex(int(maskedSeed, 16) ^ int(seedMask, 16))[2:]
    dbMask = MGF1(seed, k - hLen - 1)
    DB = hex(int(maskedDB, 16) ^ int(dbMask, 16))[2:]
   
    lPrimeHash = DB[:hLen]
    PS = DB[hLen * 2: hLen * 2 + DB[hLen * 2:].find("01") + 2]
    M = DB[hLen * 2 + len(PS):]

    return M


    
if __name__ == '__main__':
  
    mgfSeed = "9b4bdfb2c796f1c16d0c0772a5848b67457e87891dbc8214"
    maskLen = 21

    M = "c107782954829b34dc531c14b40e9ea482578f988b719497aa0687"
    seed = "1e652ec152d0bfcd65190ffc604c0933d0423381"
    
    
    EM = "0063b462be5e84d382c86eb6725f70e59cd12c0060f9d3778a18b7aa067f90b2178406fa1e1bf77f03f86629dd5607d11b9961707736c2d16e7c668b367890bc6ef1745396404ba7832b1cdfb0388ef601947fc0aff1fd2dcd279dabde9b10bfc51efc06d40d25f96bd0f4c5d88f32c7d33dbc20f8a528b77f0c16a7b4dcdd8f"
  
    print("MGF1 output: " + MGF1("9b4bdfb2c796f1c16d0c0772a5848b67457e87891dbc8214", 21))
    print("<==============================================================>")
    print("OAEP encode output: " + OAEP_encode(M, seed)) 
    print("<==============================================================>")
    print("OAEP decode output: " + OAEP_decode(EM)) 