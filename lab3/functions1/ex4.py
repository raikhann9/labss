#Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
def prime(num):
    if num<=1:
        return False
    for j in range(2,num):
        if num%j==0:
            return False
    return True
def filter_prime():
    primes=[]
    for i in numbers:
        if i.isdigit() and prime(int(i)):
            primes.append(i)
    return primes

numbers=input().split()

print(filter_prime())