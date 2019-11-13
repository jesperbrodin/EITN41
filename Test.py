'''
Created on 8 Nov 2019

@author: williamrosenberg
'''


'''
Returns i if it fills the requirements for Luhns algorithm for String number. Otherwise returns empty String





'''





def luhn(number, i):
    
    number = list(number)
    number[number.index("X")] = i    
    luhnsum = 0    
    y = len(number)-1      
    while(y > 0):
        
        luhnsum = luhnsum + int(number[y])
        tempsum = 2*int(number[y-1])
        if tempsum > 9:
            tempsum = tempsum - 9
        luhnsum = luhnsum + tempsum
        y = y - 2
    
    if luhnsum%10 == 0:
        return i    

    return ""
'''
Runs luhns algorithm for a list of numbers. Tests values of X of 0-9, 
returns a String of X values that fullfills Luhns algorithm.
'''
def testluhn(numberlist):
    s = ""
    for number in numberlist:
        x = 0
        while(x < 10):
            s = s + str(luhn(number, x))
            x = x + 1
                           
            
    return s;

def main():
    
    textfile = open("realquiztestfile.txt")
    splittextfile = (textfile.read().splitlines())
    
    print(testluhn(splittextfile))
    
    
    
           
  
if __name__== "__main__":
    main()




