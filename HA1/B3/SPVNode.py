'''
Created on 13 Nov 2019

@author: jesperbrodin & williamrosenberg
'''

import hashlib



def SPVNode (file):
   b = readFile(file)
   
   last_result = ""
   for node in range(len(b)):
       if node == 0:
          last_result = b[node]
       else:
          pathindicator = (b[node][0])
          concat = ""
          if(pathindicator == 'L'):
              concat = b[node].strip('L') + last_result
          else:
              concat = last_result + b[node].strip('R')
          last_result = (hashlib.sha1(bytearray.fromhex(concat))).hexdigest()
   
   print(last_result)


def readFile(file):
    list = []
    file = open(file) 
    for x in file:
        x = x.strip('\n')
        list.append(x)
    return list

def main():
    SPVNode("merkle1.txt")


if __name__ == '__main__':
    main()
    pass