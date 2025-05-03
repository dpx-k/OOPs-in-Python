import timeit
import math

number = 98765432123456789987654345678998765678765434567876543456787654345678765434567876543456

# Time using x ** 0.5
time_pow = timeit.timeit(lambda: number ** 0.5, number=1000000)
print(f"Time for x ** 0.5: {time_pow:.6f} seconds")

# Time using math.sqrt(x)
time_sqrt = timeit.timeit(lambda: math.sqrt(number), number=1000000)
print(f"Time for math.sqrt(x): {time_sqrt:.6f} seconds")