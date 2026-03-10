# Task:Write a function to find the sum of digits of a number.
def sum_digit(n):
    sum=0
    while n>0:
        digit=n%10 # Extracting the last digit
        sum=sum+digit
        n=n//10 # Removing the last digit
    return sum

# Taking input from the user
n=int(input("Enter any number:"))
sum=sum_digit(n)
print("The sum of the entered digit is:",sum)