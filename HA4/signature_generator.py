'''
Created on 11 Dec 2019

@author: williamrosenberg and jesperbrodin
'''


import time as kronos
import requests as req


def get_req_time(url, params):
    start = kronos.time()
    r = req.get(url, params, verify = False)
    elapsed = kronos.time() - start
    return elapsed

def get_req_time2(url, params):
  
    return req.get(url, params, verify = False).elapsed.total_seconds()
    


def calc_sig(name, grade, url):
    signature = ""
    tempsig = signature
    counter = 0
    for i in range(0, 20):
       
        max_measured_time = 0
        char_at_max_measured_time = ''
        for c in range(0, 16):
            counter = counter + 1
            c = hex(c)[2:]
           # print(c)
            tempsig2 = tempsig + c
            #print(tempsig2)
            params = {"name" : name, "grade": grade, "signature" : tempsig2}
            
            req_times = [get_req_time(url, params) for x in range(5)]
            
            
            min_req_time = min(req_times)
            #print(min_req_time)
            if min_req_time > max_measured_time:
                max_measured_time = min_req_time
                char_at_max_measured_time = c
            
            tempsig2 = tempsig
        tempsig = tempsig + char_at_max_measured_time    
        print(tempsig)    
    print(counter)    
    print(tempsig)   
    print("len = " + str(len(tempsig)))
    return tempsig





if __name__ == '__main__':
    url = "https://eitn41.eit.lth.se:3119/ha4/addgrade.php"
    name = "Kalle"
    grade = "5"
    print(calc_sig(name, grade, url))
    pass
    