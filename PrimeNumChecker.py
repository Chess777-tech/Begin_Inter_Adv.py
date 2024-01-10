# Write a function that checks if a given number is prime.


def is_prime(number):
    # Check if the number is less than 2
    if number < 2:
        return False
    
    # Check for factors from 2 to the square root of the number 
    for i in range (2, int(number**0.5) + 1):
        if number % i == 0:
            return False # The number divisible by i, so its not prime
    
    return True


test_number = 17
result = is_prime(test_number)
print(f"Is {test_number} a prime number? {result}")