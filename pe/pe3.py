n = 600851475143

# find largest prime factor of n
def pe3(n):
    # start at n //2 , go down till one number divides it, repeat?
    starting = 3
    while n % starting != 0:
        starting += 1
    print(starting / )

print(pe3(n))