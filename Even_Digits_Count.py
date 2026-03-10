# Count how many even digits are in a number using functions
# Example: Input: 2468 --->  All digits --> Output : 4
# Example: Input: 12345 ---> Even digits: 2,4 ---> Output: 2
def even_digit(n):
    count=0
    while n>0:
        digit=n%10 # Extracting the last digit from the number
        if digit %2==0:
            count=count+1
        n=n//10
    return count
n=int(input("Enter the number:"))
print("The total count of the even number from the digit {",n,"} is:",even_digit(n))