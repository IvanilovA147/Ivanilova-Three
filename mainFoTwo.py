import time

def timer_wrapper(func):
    def wrapper(n):
        start_time = time.perf_counter()
        result = func(n)
        end_time = time.perf_counter()
        print(f"Час виконання: {end_time - start_time:} секунд")
        return result
    return wrapper

def prime_generator():
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
        num += 1

@timer_wrapper
def prime_num_getter(n):
    primes = []
    gen = prime_generator()
    for _ in range(n):
        primes.append(next(gen))
    print(primes)

prime_num_getter(100000)
