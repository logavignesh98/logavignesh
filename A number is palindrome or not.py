num =int(input())
a=n
b=0
while (n>10):
    dig =n%10
    b = b*10+dig
    n =n//10
if (a==b):
    print("palindrome")
else:
    print("not a palindrome")
    
