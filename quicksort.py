def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Select pivot (choosing the last element here)
        pivot = arr[-1]
        # Partitioning the array
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]
        # Recursively sort the subarrays
        return quicksort(left) + [pivot] + quicksort(right)
