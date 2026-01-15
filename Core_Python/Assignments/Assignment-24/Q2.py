import threading

# Condition object for synchronization
condition = threading.Condition()
number = 1

def print_odd():
    global number
    while number <= 10:
        with condition:
            if number % 2 == 0:
                condition.wait()
            print("Odd Thread :", number)
            number += 1
            condition.notify()

def print_even():
    global number
    while number <= 10:
        with condition:
            if number % 2 == 1:
                condition.wait()
            print("Even Thread:", number)
            number += 1
            condition.notify()

# Create threads
t1 = threading.Thread(target=print_odd)
t2 = threading.Thread(target=print_even)

# Start threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()
