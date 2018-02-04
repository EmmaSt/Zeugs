n = (input("Bis wohin sollen Primzahlen gesucht werden?")+1)
numbers=[[],[]]
prims = []
for i in range(n):
    numbers[0].append(i)
    numbers[1].append(True)

numbers[1][1] = False
numbers[1][0] = False

z = 2
for z in range((n/2)):
    if numbers[1][z] == True:
        x = z + 1
        while x<n:
            if x % z == 0:
                numbers[1][x] = False
                x = x + 1
            else:
                x = x +1
        z = z+1

for t in range((n-1)):
    if numbers[1][t] == True:
        prims.append(numbers[0][t])
print("Primzahlen:")
print(prims)        
