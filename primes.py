lower = 1
upper = 20000

def show_primes(lower, upper):
    primes = []
    for num in range(lower,upper + 1):
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               primes.append(primes)

show_primes(lower, upper)
