# Determine if a input number is prime using a function
def get_number(promptText="Give a number: "):
    n = int(input(promptText))
    return n

def is_prime(n):
    divisors = [val for val in range(2,n) if n % val == 0]
    return divisors

user_number = get_number("Give a number higher than 2: ")
prime_check = is_prime(user_number)

if len(prime_check) == 0:
    print("Number is prime")
else:
    print("Number is not prime")
