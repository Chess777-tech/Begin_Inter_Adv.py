#Write a function that takes a string as input and returns its reverse.


def reverse_string(input_string):
    return input_string[::-1]  # slice notation means to start from the end and move backward with a step of -1.


orginal_string = "Hello World"
reversed_string = reverse_string(orginal_string)
print(f"Orginal String: {orginal_string}\n")
print(f"Reversed String: {reversed_string}")
