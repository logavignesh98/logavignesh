num =int(input())
if num>1:
    for i in range(2,num):
        if (num % i) == 0:
            print (num,"is not a prime number")
            print (i,"times",num//i,"is",num)
            break
    else:
        print(num,"num is a prime number")
else:
    print(num,"num is not a prime nummber")
