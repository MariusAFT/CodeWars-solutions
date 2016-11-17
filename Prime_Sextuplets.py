'''                     This is a description of the program requirements:

We are interested in collecting the sets of six prime numbers, that having a starting prime p, the following values 
are also primes forming the sextuplet
[p, p + 4, p + 6, p + 10, p + 12, p + 16]
The first sextuplet that we find is
[7, 11, 13, 17, 19, 23]
The second one is
[97, 101, 103, 107, 109, 113]
Given a number
sum_limit, you should give the first sextuplet which sum (of its six primes) surpasses the sum_limit value.
find_primes_sextuplet(70) == [7, 11, 13, 17, 19, 23]
find_primes_sextuplet(600) == [97, 101, 103, 107, 109, 113]'''

import time

def find_primes_sextuplet(sum_limit):

    def is_prime(nr):
        for i in range(2, nr // 2):
            if nr % i == 0:
                return False
        return True

    sir = []
    while sum_limit > 2:
        elemente_sir = {1: -4, 2: -2, 3: -4, 4: -2, 5: -4}
        if is_prime(sum_limit):
            sir.append(sum_limit)
            if len(sir) in elemente_sir:
                sum_limit += elemente_sir[len(sir)]
            else:
                return sir[::-1]
        else:
            if len(sir) > 0:
                sum_limit = sir[0] - 2
                del sir[:]
            else:
                sum_limit -= 1

start_time = time.clock()
print(find_primes_sextuplet(3000))
exec_time = time.clock() - start_time
print(exec_time)


