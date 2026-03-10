# Task to check if a number is an Armstrong number (sum of cubes of digits equals the number) using fuction
# In a simple language, armstrong number is a number in which both orginal number as well as generated number are same.
# Examples: 153 --> 1^3 + 5^3 + 3^3 = 153 (Its a Armstrong number)
# Examples: 123 ---> 1^3 + 2^3 + 3^3 = 36 (Its not a Armstrong number)

def check_arm(n):
    original=n
    store=0
    while n>0:
        digit=n%10 # Extracting a last number from the entered digit
        store=store+digit**3  # if 153, store=0+3*3*3 =27,store=27+5*5*5=152, store=152+1*1*1=153
        n=n//10 # Removing a last number from the entered digit
    return store==original

# Input from the user
n=int(input("Enter the any Digits:"))
if check_arm(n):
    print(n," is an Armstrong number")
else:
    print(n," is not an Armstrong number")


# Checking list of elements(data)
print("\nElemnets check-")
list_of_elements=[123,234,153,36,370]
for i in list_of_elements:
    if check_arm(i):
        print(i," is an Armstrong Number.")
    else:
        print(i," is not a Armstrong Number.")