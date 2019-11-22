'''
Created on 21 Nov 2019

@author: williamrosenberg and jesperbrodin
'''
import hashlib
import math

class MerkleTree:
    
    # Takes a textfile and extracts i, j and leaves from it. Also creates variables needed
    # for building tree.
    def __init__(self,textfile):
        textfile = open(textfile)
        self.i = int(textfile.readline())
        self.j = int(textfile.readline())
        self.leaves = (textfile.read().splitlines())
        self.pathNodeAtInputIndex = ""
        self.root = ""
        self.pathParentIndex = self.i
        self.merklePath = []
    
    # Prints the merkle path node at depth j, concatenated with the merkle root 
    def printResults(self):
        result = self.merklePath[len(self.merklePath) - self.j] + self.root
        print(result)
    
    # Recursively builds the tree and saves the merkle path of node i in self.merklepath. Takes leaves and 
    # pathParentIndex as parameters. pathParentIndex will be i in the first round, and later on will take
    # on the index of the parent of node at i. 
    def buildtree(self, leaves, pathParentIndex):
        nextLevelBranches = []
        if(len(leaves) == 1 ):
            self.root = leaves.pop()
            return
            
        if(len(leaves)%2 != 0):
            leaves.append(leaves[len(leaves)-1])
        
        for index in range(0, len(leaves)-1, 2):
            if(index == pathParentIndex):
                rightleaf = "R" + leaves[index+1]
                self.merklePath.append(rightleaf)
                pathParentIndex = len(nextLevelBranches)
                  
            elif(index + 1 == pathParentIndex):
                leftleaf = "L" + leaves[index]
                self.merklePath.append(leftleaf)
                pathParentIndex = len(nextLevelBranches)
                    
            concatNodes = leaves[index] + leaves[index+1]
            hashedConcatNode = (hashlib.sha1(bytearray.fromhex(concatNodes))).hexdigest()
            nextLevelBranches.append(hashedConcatNode)

        self.buildtree(nextLevelBranches, pathParentIndex)

if __name__ == '__main__':
    
    # Enter chosen textfile as parameter into MerkleTree below
    merkleTree = MerkleTree("testleaves79.txt")
    
    # Build the tree
    merkleTree.buildtree(merkleTree.leaves, merkleTree.pathParentIndex)
    
    #Print results
    merkleTree.printResults()
    pass
    
    