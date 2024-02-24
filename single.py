import random
import time

# Generate an array of 100 random integers ranging between 0 and 300
array = [random.randrange(0, 500) for _ in range(100)]

# Measure the time taken to sort the array
start_time = time.time()
time.sleep(1)
array.sort()
time.sleep(1)
end_time = time.time()

# Print the time taken and the sorted array

print("Sorted array:", array)
print("Time taken:", end_time - start_time-2, "seconds")
