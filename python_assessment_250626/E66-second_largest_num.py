#Input: 1,2,3,4,5 expected output: 4 
# Input: -1,-2,-3,-4, -5 expected output: -2

def second_largest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    if len(unique_numbers) < 2:
        return None  # Not enough unique numbers for a second largest
    unique_numbers.sort(reverse=True)  # Sort in descending order
    return unique_numbers[1]  # Return the second largest number

print(second_largest([1, 2, 3, 4, 5]))
print(second_largest([-1, -2, -3, -4, -5])) 