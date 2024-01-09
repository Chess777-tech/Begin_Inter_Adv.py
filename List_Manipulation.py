"""
Python program that creates a list of numbers and prints the sum, average, maximum, and minimum of those numbers:

"""


# Create a list of numbers
nums = [1,2,3,4]


# Calculate and print the sum
sum_nums = sum(nums)
print(f"Sum: {sum_nums}")


# Calculate and print the average 
avg = sum_nums / len(nums)
print(f"Avg: {avg:.2f}")    # .2f specifices that you wanat to format the float w/ two decimal places


# Print the max and min
maximum = max(nums)
minimum = min(nums)
