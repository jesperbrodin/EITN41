'''
Created on 13 Nov 2019

@author: jesperbrodin
'''

import hashlib



def SPVNode (merkle):
   b = bytearray.fromhex(merkle)
   for a in b:
       print(a)
    
   
   
   ''' hashresult = ""
    for index in range(len(merkle)): 
        merkle[index+1] = merkle[index+1] + merkle[index]
        hashlib.sha1(merkle[index + 1])
    return merkle[index + 1]
'''

def main ():
    text = ""
    file = open("merkle.txt") 
    for x in file:
        text = text + x
    print(text)


if __name__ == '__main__':
    main()
    pass