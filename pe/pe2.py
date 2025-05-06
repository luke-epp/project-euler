def pe2(n):
    # find sum of fib numbers below n

    # do dp approach
    fib_list = [0] * (n)
    fib_list[0] = 1
    fib_list[1] = 2
    for i in range(2,len(fib_list)-1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
        if fib_list[i] > n:
            fib_list[i] == 0
            break
    
    fib_list = [x if x % 2 == 0 else 0 for x in fib_list]
    return (sum(fib_list))

print(pe2(4000000))