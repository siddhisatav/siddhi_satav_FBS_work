import threading
import time
import random

# Shared buffer
buffer = []
BUFFER_SIZE = 5

# Condition object for synchronization
condition = threading.Condition()

# Producer function
def producer(name):
    global buffer
    while True:
        item = random.randint(1, 100)  # Produce a random item
        with condition:
            while len(buffer) >= BUFFER_SIZE:
                condition.wait()  # Wait if buffer full

            buffer.append(item)
            print(f"{name} produced: {item} | Buffer: {buffer}")
            condition.notify_all()  # Notify consumers

        time.sleep(random.random())  # Simulate production time

# Consumer function
def consumer(name):
    global buffer
    while True:
        with condition:
            while len(buffer) == 0:
                condition.wait()  # Wait if buffer empty

            item = buffer.pop(0)
            print(f"{name} consumed: {item} | Buffer: {buffer}")
            condition.notify_all()  # Notify producers

        time.sleep(random.random())  # Simulate consumption time

# Create threads
producers = [threading.Thread(target=producer, args=(f"Producer-{i+1}",)) for i in range(2)]
consumers = [threading.Thread(target=consumer, args=(f"Consumer-{i+1}",)) for i in range(2)]

# Start threads
for t in producers + consumers:
    t.start()

# Optional: join threads (will run infinitely unless stopped)
# for t in producers + consumers:
#     t.join()
