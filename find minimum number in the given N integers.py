def smallest num in list (list):
    min= list[0]
    for a in list:
        if a < min:
             min = a
    return min
print (smallest num in list([2,3,1,45,5]))
