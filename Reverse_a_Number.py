#Write a function that returns the reverse of a number
def reverse_num(n):
    reverse=0
    while n>0:
        digit=n%10 # Extracting the last number
        reverse=reverse*10+digit # if n=12, reverse=0*10+2=2, reverse=2*10+1=21
        n=n//10 # Remvoing the last digit
    return reverse

n=int(input("Enter any digits:"))
print("The reverese order of digit ",n," is:",reverse_num(n))