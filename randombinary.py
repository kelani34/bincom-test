####################----- 8. RANDOM BINARY-----########################
from random import randint

random_num = randint(1000, 9999)
print(random_num)
def base10tobase2(num):
    if num >= 1:
        base10tobase2(num // 2)
    print(num % 2, end='')
    return num % 2

num = base10tobase2(random_num)
print(num)
numd = str(num)
def base2tobase10(num):
    binary_num = num
    dec_num = int(binary_num, 2)
    return dec_num
print(base2tobase10(numd))