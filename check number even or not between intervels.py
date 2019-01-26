even = [int(x) for x in input().split()]
for number in range(1,11):
    if number % 2 == 0:
        even.append(number)
print ("even numbers",even)
