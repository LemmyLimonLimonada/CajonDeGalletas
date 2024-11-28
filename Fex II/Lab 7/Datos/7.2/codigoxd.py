path = 'datos7.2.txt'
path_2 = 'datos_nuevos.txt'
lista = []
lista_2 = []

with open(path, 'r') as dato:
            datos = dato.readlines()
            for i in datos:
                lista.append(i.strip())

for i in lista[1:]:
    numero = i.split(',')
    diferencia = round(float(numero[0])- float(numero[1]), 3)
    i = str(numero[0]) + ',' + str(numero[1]) + ',' + str(diferencia) + ',' + str(numero[2]) + '\n'
    lista_2.append(i)

print(lista_2)

with open(path_2, 'w') as archivo:
       for i in lista_2:
           archivo.write(i)