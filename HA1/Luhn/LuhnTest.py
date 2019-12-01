@author: williamrosenberg
'''
def luhn(number, i):
    print("innan modulo") 
    
    
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
        print("Tummen upp xD")
        print(number)
        return i    

    
def testluhn(numberlist):
    s = ""
    for number in numberlist:
        x = 0
        while(x < 10):
            s = s + string(luhn(number, x)
                           
    return s    

def main():
    
    
    testlist = ["12774212857X4109", "586604X108627571"]
    testluhn(testlist)    
    return         
  
if __name__== "__main__":
    main() '''
