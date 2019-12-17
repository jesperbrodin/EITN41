'''
Created on 16 Dec 2019

@author: williamrosenberg and jesperbrodin
'''
import base64

#These two are from Stack Overflow:
#https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

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


    
def RSA(p, q, e = 65537):
    v = 0;
    n = p * q
    d = modinv(e, (p - 1) * (q - 1))
    e1 = d % (p - 1)
    e2 = d % (q - 1)
    c = modinv(q, p)

    v_DER = der_encode(v)
    n_DER = der_encode(n)
    e_DER = der_encode(e)
    d_DER = der_encode(d)
    p_DER = der_encode(p)
    q_DER = der_encode(q)
    e1_DER = der_encode(e1)
    e2_DER = der_encode(e2)
    c_DER = der_encode(c)

    enc_RSA = v_DER + n_DER + e_DER + d_DER + p_DER + q_DER + e1_DER + e2_DER + c_DER

    RSA_key = der_encode(int(enc_RSA, 16))
    RSA_key = "30" + RSA_key[2:]

    return base64.b64encode(bytearray.fromhex(RSA_key))




if __name__ == '__main__':
    a = 161863091426469985001358176493540241719547661391527305133576978132107887717901972545655469921112454527920502763568908799229786534949082469136818503316047702610019730504769581772016806386178260077157969035841180863069299401978140025225333279044855057641079117234814239380100022886557142183337228046784055073741

    p = 2530368937
    q = 2612592767
    print(der_encode(a))
    print("<--------------------------------------------------------------------------->")
    print("<--------------------------------------------------------------------------->")
    print(RSA(p, q))
    pass