import cirq


# def less_than_circuit(numbers, input_value):


    # return list of numbers less than K

    # Return circuit diagram

# def proof_of_better_than_classical():
#     count = 0
#     for num in lst:
#         if num < k:
#             count += 1
#     return count


import time
import matplotlib.pyplot as plt
import numpy as np

import time
import matplotlib.pyplot as plt
import numpy as np

def count_integers_less_than_k(lst, k):
    count = 0
    for num in lst:
        if num < k:
            count += 1
    return count

def measure_execution_time(n_values):
    execution_times = []
    for n in n_values:
        numbers = list(range(n))
        start_time = time.time()
        count_integers_less_than_k(numbers, n//2)  # assuming k is approximately n/2
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
    return execution_times

# Generate different sizes of input lists
n_values = [10**i for i in range(0, 6)]

# Measure execution time for each input size
execution_times = measure_execution_time(n_values)
print(execution_times)

# Plot the relationship between input size and execution time
plt.plot(n_values, execution_times, marker='o')
plt.title('Execution Time vs Input Size (Log Scale)')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.xscale('log')  # Use logarithmic scale for x-axis
plt.yscale('log')  # Use logarithmic scale for y-axis
plt.grid(True)
plt.show()


