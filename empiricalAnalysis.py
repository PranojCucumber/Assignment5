import random
import time
import numpy as np

# Deterministic Quicksort
def quicksort(arr):
    while len(arr) > 1:
        pivot = arr[-1]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        # Recur on the smaller partition to limit recursion depth
        if len(left) < len(right):
            return quicksort(left) + middle + right
        else:
            return left + middle + quicksort(right)
    return arr



# Randomized Quicksort
def randomized_quicksort(arr):
    while len(arr) > 1:
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        # Recur on the smaller partition to limit recursion depth
        if len(left) < len(right):
            return randomized_quicksort(left) + middle + right
        else:
            return left + middle + randomized_quicksort(right)
    return arr



# Measure runtime
def measure_runtime(func, arr):
    start_time = time.time()
    func(arr.copy())
    return time.time() - start_time

# Generate different input distributions
def generate_inputs(size):
    random_array = np.random.randint(0, 100000, size).tolist()  # Random input
    sorted_array = sorted(random_array)                         # Sorted input
    reverse_sorted_array = sorted(
        random_array, reverse=True)   # Reverse-sorted input
    return random_array, sorted_array, reverse_sorted_array

# Run the empirical analysis
def empirical_analysis():
    sizes = [1000, 5000, 10000]  # Different input sizes
    results = []

    for size in sizes:
        random_array, sorted_array, reverse_sorted_array = generate_inputs(
            size)

        for array_type, array in zip(["Random", "Sorted", "Reverse-Sorted"],
                                     [random_array, sorted_array, reverse_sorted_array]):
            det_time = measure_runtime(quicksort, array)
            rand_time = measure_runtime(randomized_quicksort, array)

            results.append({
                "Size": size,
                "Array Type": array_type,
                "Deterministic Time (s)": det_time,
                "Randomized Time (s)": rand_time
            })

    # Print results
    print(f"{'Size':<10}{'Array Type':<15}{'Deterministic Time (s)':<25}{'Randomized Time (s)':<25}")
    for result in results:
        print(f"{result['Size']:<10}{result['Array Type']:<15}"
              f"{result['Deterministic Time (s)']:<25.5f}{result['Randomized Time (s)']:<25.5f}")


# Run the analysis
empirical_analysis()
