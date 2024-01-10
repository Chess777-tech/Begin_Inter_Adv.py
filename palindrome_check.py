# Write a function that checks if a given string is a palindrome.


def is_palindrome(input_string):
    # Convert the string to lowercase to make check case-insensitive
    cleaned_string = input_string.lower()

    # Remove non-alphanumeric characters 
    cleaned_string = ''.join(char for char in cleaned_string if char.isalnum())

    # Check if the cleaned string is equal to its reverse 
    return cleaned_string == cleaned_string[::-1]


test_string = " A man, a plan, a canal, Panama!"
result = is_palindrome(test_string)
print(f"Is '{test_string}' a palindrome? {result}")