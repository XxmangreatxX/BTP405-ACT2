def primeNumbersBetween(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primeNumbers(n):
    return [i for i in range(2, n+1) if primeNumbersBetween(i)]

n = 100
primeNums = primeNumbers(n)

print("Prime numbers between 2 and {n}:")
print(primeNums)