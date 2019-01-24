year = int(input(''))
if year % 4 == 0 and year % 100 != 0:
    print(year,"leap year")
elif year % 100 == 0:
    print(year,"is not a leap year")
elif year % 400 == 0:
    print(year,"is leap year")
else:
    print(year,"is not a leap year")
