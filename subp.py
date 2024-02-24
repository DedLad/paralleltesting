import random
import time
import multiprocessing
def sort_subarray(arr):
    arr.sort()
    return arr

if __name__ == '__main__':
    # Generate the array of random integers
    arr = [random.randrange(0, 500) for _ in range(100)]

    # Split the array into 10 subarrays
    subarrays = [arr[i:i+10] for i in range(0, len(arr), 10)]

    # Create a multiprocessing pool with 100 processes
    pool = multiprocessing.Pool(processes=10)

    # Start the timer
    start_time = time.time()

    # Sort each subarray using multiprocessing
    sorted_subarrays = pool.map(sort_subarray, subarrays)

    # Concatenate the sorted subarrays into a single sorted array
    sorted_arr = [num for subarr in sorted_subarrays for num in subarr]

    # Stop the timer
    end_time = time.time()

    # Print the sorted array and the time taken
    print("Sorted Array:", sorted_arr)
    print("Time Taken:", end_time - start_time, "seconds")
