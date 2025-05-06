


find_primes_below_n = function(n){
    prime_list = 2:(n-1)
    check = round(sqrt(n))
    for (divisor in 2:check){
        prime_list = prime_list[prime_list == divisor | prime_list %% divisor !=0]
    }
    return(prime_list)
}

n = 2000000

primes = find_primes_below_n(n)
print(primes)
print(sum(primes))
