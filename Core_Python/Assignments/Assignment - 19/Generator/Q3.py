# 3. Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.

def rangee(start ,stop,step):
    curr = start
    if step > 0 :
        while curr < stop:
            yield curr
            curr+=step
    elif step < 0 :
        while curr > stop :
            yield curr
            curr+=step


# Example usage
for num in rangee(1, 10, 2):
    print(num, end=" ")
