def power(base,expo):
    if(expo==1):
        return (base)
    if(expo!=1):
        return (base*power(base,expo-1))
base = int(input())
expo = int(input())
print ("Result=",power(base,expo))
        
