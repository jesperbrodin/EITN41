'''
Created on 16 Dec 2019

@author: williamrosenberg and BigJeba1337

'''

def der_encode(a):
    T = "02"
    L = ""
    V = hex(a)[2:]
    
    if(len(V) % 2 != 0):
        V = "0" + V
    if(int(V[0], 16) >= 8):
        V = "00" + V
    
    v_length = int(len(V)/2)
    temp_l = hex(v_length)[2:]
    
    if int(len(temp_l) % 2 != 0):
        temp_l = "0" + temp_l
    
    if v_length in range(0, 127):
        if len(temp_l) == 1:
            v_length = "0" + temp_l
            
        else:
            v_length = temp_l
        L = v_length  
      
    elif v_length > 127:
        if(len(temp_l) % 2 == 0):
            a = int(len(temp_l)/2)
        else:
            a = 1 + int(len(temp_l)/2)
        L = "8" + hex(a)[2:] + temp_l
        
    return T + L + V 
    
    
if __name__ == '__main__':
    print(der_encode(161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741))
    pass