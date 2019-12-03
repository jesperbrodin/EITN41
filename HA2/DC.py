'''
Created on 27 Nov 2019

@author: williamrosenberg
'''


def diningc(abitu, abitb, bbita, bbitu, ubita, ubitb, payer):
    absecret = abitb ^ bbita
    ausecret = abitu ^ ubita
    ubsecret = ubitb ^ bbitu
    
    axor = absecret ^ ausecret
    bxor = absecret ^ ubsecret
    uxor = ausecret ^ ubsecret
    
    if(payer == 'a'):
        axor = axor ^ 1
    elif(payer == 'b'):
        bxor = bxor ^ 1
    elif(payer == 'c'):
        uxor = uxor ^ 1
    
    
    result = axor ^ bxor ^ uxor    


def hex_to_binary(hexstring):
    
    return bin(int(hexstring, 16))[2:].zfill(16)

def binary_to_hex(binstring):
    
    return hex(int(binstring, 2)).zfill(4).upper()
    

def toBin(data):
    return int(data, 16)

def dc(dining_data):
    SA = toBin(dining_data.get("SA"))
    SB = toBin(dining_data.get("SB"))
    DA = toBin(dining_data.get("DA"))
    DB = toBin(dining_data.get("DB"))
    M = toBin(dining_data.get("M"))
    b = dining_data.get("b")
    
    res = hex(SA ^ SB ^ M)[2:]
    res = res.zfill(4)
    
    
    if(b == 1):
        return res
    
    else:
        xor1 = SA ^ SB
        xor2 = DA ^ DB
        xor3 = xor1 ^ xor2
        
        xor3 = hex(xor3)[2:]
        xor1 = hex(xor1)[2:]
        return (str(xor1) + str(xor3)).upper()
        


if __name__ == '__main__':
    data_1 = {
        "SA": "70A8",
        "SB": "9483",
        "DA": "C068",
        "DB": "86B7",
        "M": "6109",
        "b": 0
}
    print(dc(data_1))
    
    pass