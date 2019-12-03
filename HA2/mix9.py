'''
Created on 30 Nov 2019

@author: williamrosenberg and jesperbrodin


Note: The algorithm for the function exclusion_phase was inspired by the code found here:
https://github.com/Nerja/EITN41/blob/master/Assignments/Assignment2/B-2/main.py


'''
import pcapfile
import struct
import socket
from pcapfile import savefile

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]



def read_file():
    
    testcap = open('cia.pcap', 'rb')
    capfile = savefile.load_savefile(testcap, layers=2, verbose=True)

    # print the packets
    #print ('timestamp\teth src\t\t\teth dst\t\t\tIP src\t\tIP dst')

    pkt_list = []

    for pkt in capfile.packets:
        timestamp = pkt.timestamp
        # all data is ASCII encoded (byte arrays). If we want to compare with strings
        # we need to decode the byte arrays into UTF8 coded strings
        eth_src = pkt.packet.src.decode('UTF8')
        eth_dst = pkt.packet.dst.decode('UTF8')
        ip_src = pkt.packet.payload.src.decode('UTF8')
        ip_dst = pkt.packet.payload.dst.decode('UTF8')
        #print ('{}\t\t{}\t{}\t{}\t{}'.format(timestamp, eth_src, eth_dst, ip_src, ip_dst))
    
        a = {
            "eth_src" : eth_src,
            "eth_dst" : eth_dst,
            "ip_src" : ip_src,
            "ip_dst" : ip_dst
            }
        pkt_list.append(a)
        
    #print(pkt_list)
    return (pkt_list)

def find_nbr_pkts_in_batch(packetlist):
    nbr = 0
    
    for x in packetlist:
        if(x.get("ip_dst") == packetlist[packetlist.index(x)+1].get("ip_dst")):
            nbr = nbr + 1
        else:
            nbr = nbr + 1
            break
   
    return nbr*2
    
    pass

def sort_packets(packetlist, nazir_ip):
    nbrinbatch = find_nbr_pkts_in_batch(packetlist)
    
    batchlist = []
    for x in range(0, len(packetlist), nbrinbatch):
        batch = []
        for y in range(x, x+nbrinbatch):
            batch.append(packetlist[y])    
        a, b = split_list(batch)
        c = [a, b]   
        batchlist.append(c)       
    
    interesting_batches_list = []    
    for x in batchlist:
        for y in x[0]:
            if(y.get("ip_src") == nazir_ip):
                interesting_batches_list.append(x[1])
                

    #Convert Packet objects to their dest_ip:s
    
    ip_list = []
    
    for i in range(0, len(interesting_batches_list)):
        temp_ip_list = set()
        for z in range(0, len(interesting_batches_list[0])):
            temp_ip_list.add(interesting_batches_list[i][z].get("ip_dst"))        
        ip_list.append(temp_ip_list)
    
    return ip_list
    
def find_m_disjoint_sets(int_batches, m):
    disjoint_sets = []
    while len(disjoint_sets) < m:
        for i in range(0, len(int_batches)):
            if new_set_is_disjoint(disjoint_sets, int_batches[i]):
                disjoint_sets.append(int_batches[i])
          
    return disjoint_sets
            
def new_set_is_disjoint(disjoint_sets, new_set):
    return all([s.isdisjoint(new_set) for s in disjoint_sets])

def exclusion_phase(disjoint_sets, int_batches):
    for r in int_batches:
        i = -1
        duplicate_ip = False
        for rx in range(len(disjoint_sets)):
            if not r.isdisjoint(disjoint_sets[rx]):
                if i == -1:
                    i = rx
                else:
                    duplicate_ip = True
                    break
                
        if not duplicate_ip and not i == -1:
            disjoint_sets[i] = disjoint_sets[i].intersection(r)
    
        if (all(len(x) == 1 for x in disjoint_sets)):
            break
    
    return disjoint_sets

def ip_integer_sum(ip_list):
    ipsum = 0
    for x in ip_list:
        for i in x:
        
            packedIP = socket.inet_aton((i))
            ipsum = ipsum + struct.unpack("!L", packedIP)[0]
    return ipsum    

if __name__ == '__main__':
    
    # Input data
    read_pcap = read_file()
    nazir_ip = "61.152.13.37"
    mix_ip = "95.235.155.122"
    nbr_partners = 8
    
    # Learning phase
    int_batches = sort_packets(read_pcap, nazir_ip)
    disjoint_sets = find_m_disjoint_sets(int_batches, nbr_partners)
    
    #Exclusion phase
    suspects = exclusion_phase(disjoint_sets, int_batches)
    print(suspects)
    #Calculate and print integer IP sum
    suspect_ip_sum = ip_integer_sum(suspects)
    print(suspect_ip_sum)
    
    pass



