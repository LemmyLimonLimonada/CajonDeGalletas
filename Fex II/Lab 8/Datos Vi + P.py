path = 'Datos VI.txt'
path_2 = 'Datos VIP.txt'
lista = []
lista_2 = []

with open(path, 'r') as dato:
            datos = dato.readlines()
            for i in datos:
                lista.append(i.strip()) #Cargamos todos los datos a lista 1

for i in lista[1:]:
    linea = i.split(',') #linea de texto pasa a lista de los elementos separados por ','  
    linea.append(str(round(float(linea[0]) * float(linea[1])/1000, 3))) #manejamos la linea
    linea[0] = str(round(float(linea[0])/100,3))
    nueva_linea = ",".join(linea)
    lista_2.append(nueva_linea)
        

with open(path_2, 'w') as archivo:
       archivo.write('Voltaje(uV x 10),Intensidad(uA),Potencia(nW)')
       for dato in lista_2:
           archivo.write('\n' + dato)