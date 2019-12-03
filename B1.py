from random import randint

K_SIZE = 16

def k_generate():
    k = ""
    for x in range(K_SIZE):
        k += str(randint(0,1))
    return k





if __name__ == '__main__':
    bajs = 0