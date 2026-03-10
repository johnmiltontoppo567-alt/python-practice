# Write a function to count how many digits are in a number.
# Example: input 123 ---> Output: 3 and input 98765 ----> Output:5

def count_digit(n):
    count=0
    while n>0:
        digit=n%10 # Extracting the last digit from the entered digit
        count=count+1 # counting the digits (Iteration)
        n=n//10 # Removing a last difit from the entered digit
    return count

# Input from the user to enter the any digits
n=int(input("Enter any Digits:"))
print("The count of the entered digit ",n," is:",count_digit(n))