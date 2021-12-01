import math

def is_prime(num):
    prime = True
    for i in range(2,math.floor(math.sqrt(num))+1):
        if num%i == 0:
            prime = False
    return prime

def print_primes(number_of_primes):
    count = 0
    number = 2
    while count != number_of_primes:
        if(is_prime(number)):
            print(number)
            count+=1
        number += 1
if __name__ == '__main__':
    number_of_primes = 25
    print_primes(number_of_primes)