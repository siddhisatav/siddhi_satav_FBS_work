import threading
import time

def print_lowercase():
    for ch in range(ord('a'), ord('z') + 1):
        print("Lowercase Thread:", chr(ch))
        time.sleep(0.1)

def print_uppercase():
    for ch in range(ord('A'), ord('Z') + 1):
        print("Uppercase Thread:", chr(ch))
        time.sleep(0.1)

# Create threads
t1 = threading.Thread(target=print_lowercase)
t2 = threading.Thread(target=print_uppercase)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()
