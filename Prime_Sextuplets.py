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


