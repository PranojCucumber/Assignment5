import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Choose a random pivot
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        # Partitioning the array
        left = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
        right = [x for i, x in enumerate(arr) if x > pivot]
        # Recursively sort the subarrays
        return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)
