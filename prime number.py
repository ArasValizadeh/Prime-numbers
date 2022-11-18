def CheckAval (number):
    counter = 0
    ma = int((number/2)+2)
    for i in range (1,ma):
        baghi = number % i
        if baghi == 0 :
            counter += 1
    if counter == 1 :
        return number 
a = int(input())
b = int(input())
ListAdad = []
aval = []
for i in range (a+1,b):
    ListAdad.append(i)
for i in ListAdad:
    if CheckAval(i) ==  i :
        aval.append(i)
print(*aval,sep=',')