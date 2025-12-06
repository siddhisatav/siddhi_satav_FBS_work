# 9. Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

def three_number_combinations(numbers, target):
    result = []
    n = len(numbers)
    
    # Check all possible combinations of 3 numbers
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if numbers[i] + numbers[j] + numbers[k] == target:
                    result.append((numbers[i], numbers[j], numbers[k]))
                    
    return result


numbers = [1, 2, 3, 4, 5]
target = 9

combinations_list = three_number_combinations(numbers, target)
print("Unique combinations of 3 numbers adding up to", target, ":", combinations_list)
