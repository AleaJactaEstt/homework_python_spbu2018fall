from random import randint

list_length = randint(0, 21)
rand_list = [randint(10,21) for i in range(list_length)] 
print(rand_list)
for i in range(list_length):
    if rand_list[i] in rand_list[:i]:
        print('YES')
    else:
        print('NO')