start = int(input())
end = int(input())
for val in range(start,end+1):
    if val>1:
        for n in range(2, val):
            if (val%2) == 0:
            break
        else:
            print(val)
