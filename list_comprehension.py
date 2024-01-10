# Generate a list of squares for even numbers in the range 1 to 10 using list comprehension


squares_of_evens = [x**2 for x in range(1,11) if x % 2 == 0]

print(squares_of_evens)