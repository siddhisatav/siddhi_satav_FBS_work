import threading

# Shared list to store results from each thread
results = []

# Function to calculate sum of squares for a given range
def sum_of_squares(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i * i
    results.append(total)

# Creating 4 threads with equal ranges
t1 = threading.Thread(target=sum_of_squares, args=(1, 25))
t2 = threading.Thread(target=sum_of_squares, args=(26, 50))
t3 = threading.Thread(target=sum_of_squares, args=(51, 75))
t4 = threading.Thread(target=sum_of_squares, args=(76, 100))

# Start threads
t1.start()
t2.start()
t3.start()
t4.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()
t4.join()

# Combine results
total_sum = sum(results)

print("Sum of squares from 1 to 100 =", total_sum)
