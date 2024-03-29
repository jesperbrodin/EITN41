
# Created on 11 Nov 2019

# @author: williamrosenberg & jesperbrodin

from random import randint




#  Takes the values
#  u: number of bins = 2^u
#  k: required amount of balls in a single bin to generate 1 coin 
#  c number of coins to be generated
#  returns the number of iterations (throws) required to generate c coins.

def Mint(u, k, c):
    nbrOfBins = 2 ** u 
    bins = [0] * nbrOfBins
    genCoins = 0
    iterations = 0
    
    
    while(genCoins < c):
        iterations += 1
        rand = randint(0, nbrOfBins-1)
        bins[rand] = bins[rand] + 1
        if bins[rand] == k: genCoins = genCoins + 1
    
    return iterations


# Calculates the mean value of iterations (throws) required to generate c coins 
# returns the mean value.
def meanMint(u,k,c, iterations):
    x = 0
    sum = 0
    mean = 0
    while(x < iterations):
        sum += Mint(u,k,c)
        x += 1
        
    mean = sum/iterations
    return mean


def main(): 
    print("Mean nbr of iterations: " + str(meanMint(16, 2, 1, 10000)))
    

if __name__ == '__main__':
    main()
    pass