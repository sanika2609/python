def is_armstrong(num):
    # Convert number to string to count the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Sum of the digits raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return sum_of_powers == num

# Test the function with a range of numbers
for number in range(100, 1000):
    if is_armstrong(number):
        print(f"{number} is an Armstrong number")
