#Pedimos el numero
n = int(input())
#establecemos las condiciones
a = n % (n - ((n // 100) * 100)) == 0
print(a)
b = (n // 10000) < ((n - ((n // 1000) * 1000)) // 100)
print(b)
c = (((n - ((n // 10000) * 10000)) // 1000) > (n - (n // 10) * 10))
print(c)
d = (((n - ((n // 100) * 100)) // 10) <= (n - (n // 10) * 10))
print(d)
#verificar que sea lenny
if a == True and b == True and c == True and d == True:
    print('LENNY!')
else:
    print('NOT LENNY!')