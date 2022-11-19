def CheckAval (number):
    if number != 1 :
        counter = 0
        ma = number
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
