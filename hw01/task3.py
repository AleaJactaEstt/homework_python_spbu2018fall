from random import randint

list_length = randint(40, 61) 

rand_list = [randint(-100,102) for i in range(list_length)] 


def task3(rand_list): 
    fst = len(list(filter(lambda x: x%4 == 3,rand_list)))
    return fst

def count_bits(number):
    N = abs(number)
    M = 0
    count = 0
    while not N == 0:
        count += N % 2 
        N = N//2 
    return count + (1 if number < 0 else 0)