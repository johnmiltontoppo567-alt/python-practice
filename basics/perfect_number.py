# Write a function to check if a number is prefect (sum of its divisiors equal the number itself)
# example: what are the number divisble by 6 and their sum of the divisor should be 6 ----> 1,2,3 =6
# if the above term statisfies its considered to be perfect number.

def check_pre_num(n):
    sum=0
    for i in range(1,n-1):
        if i%2==0:
            sum=sum+i
    if sum == n:
        return True
    else:
        return False
    
#Input from the user 
print("\t Checking the number whether its perfect or not.")
n=int(input("Enter any number:"))
if check_pre_num(n):
    print(n," is a perfect number.")
else:
    print(n," is not a perfect number.")