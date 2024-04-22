import gato

#v1.3

def menu_dificulad():
    print("""\

    *** Selecciona la dificultad ***      
        [1] Facil
        [2] Intermedio
        [3] Dificil  
                        """)

def menu_inicio(ejercito_aliado, opciones, opcion):
    print("""\

 /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ 
( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )
 > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 
 /\_/\                                                          /\_/\ 
( o.o )   _____                  _        _     _     _        ( o.o )
 > ^ <   |     |___ ___ _ _    _| |___   |_|___|_|___|_|___     > ^ < 
 /\_/\   | | | | -_|   | | |  | . | -_|  | |   | |  _| | . |    /\_/\ 
( o.o )  |_|_|_|___|_|_|___|  |___|___|  |_|_|_|_|___|_|___|   ( o.o )
 > ^ <                                                          > ^ < 
 /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\  /\_/\ 
( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )( o.o )
 > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ <  > ^ < 
                                            macking cheese             
                        """)
    print(f'Dinero disponible: {ejercito_aliado._oro}')
    print(f'Ronda actual: {ejercito_aliado.ronda}')
    print("""                                                   
          [1] Tienda                                            
          [2] Ejercito                    
          [3] Combatir    

          [0] Salir del programa 

          Indique su opcion:
                    """)
    while opcion not in  opciones[0:4]:
        opcion = str(input())
        if opcion not in  opciones[0:4]:
            print('Selecione una opcion valida')
    return opcion

def menu_tienda(ejercito_aliado, opciones, opcion):
    opcion = None
    print(f"""\

         _____                  _        _   _           _           ,    ,
        |     |___ ___ _ _    _| |___   | |_|_|___ ___ _| |___      | \--/ |
        | | | | -_|   | | |  | . | -_|  |  _| | -_|   | . | .'|     ( (0_0)(
        |_|_|_|___|_|_|___|  |___|___|  |_| |_|___|_|_|___|__,|      \==Y==/  
                                                                     /'-"-'>
            Dinero disponible: {ejercito_aliado._oro}                                  _/ < ; (;
            Ronda actual: {ejercito_aliado.ronda}                                       / ,_ |_|_\\
                                                                  ( _,,)\,,),)
                Producto:                         Precio:          \ '.___
          [1] Gato Mago                             11              '-----'
          [2] Gato Guerrero                         9         
          [3] Gato Caballero                        10              
          [4] Item Armadura                         6               
          [5] Item Pergamino                        7
          [6] Item lanza                            5
          [7] Curar Ejercito                        7

          [0] Volver al Menu de inicio

          Indique su opcion:
                    """)
    while opcion not in  opciones:
        opcion = str(input())
        if opcion not in  opciones:
            print('Selecione una opcion valida')
    return opcion

def seleccion_gato(Ejercito):
    print("""\

        +-----------------------------------------------------------------+
        | _____     _             _              _                _       |
        ||   __|___| |___ ___ ___|_|___ ___    _| |___    ___ ___| |_ ___ |
        ||__   | -_| | -_|  _|  _| | . |   |  | . | -_|  | . | .'|  _| . ||
        ||_____|___|_|___|___|___|_|___|_|_|  |___|___|  |_  |__,|_| |___||
        |                                                |___|            |
        +-----------------------------------------------------------------+
       
                Clase                   Nombre
                    """)
    
    for numero_gato in range(len(Ejercito)):
        print(f'            [{numero_gato + 1}] {Ejercito[numero_gato].clase}                {Ejercito[numero_gato].nombre}    ')
              
    print("""\
        Indique su opcion:
                    """)

def continuar(opcion_aux):
    input('\nAprete cualquier boton para continuar! \n')
    opcion_aux = None

if __name__ == '__main__':
    fin_programa = False
    opciones = ['0', '1', '2', '3', '4', '5', '6', '7']
    opcion = None
    archivo_dificultad = ['facil', 'intermedio', 'dificil']
    ejercito_aliado = gato.Ejercito()
    ejercito_enemigo = gato.Ejercito()

    menu_dificulad()
    while opcion not in  opciones[1:4]:
        opcion = str(input())
        if opcion not in  opciones[1:4]:
            print('Selecione una opcion valida')
    print(f'Se seleciono la dificultad: {archivo_dificultad[int(opcion)-1]}')
    rondas_faltantes = (ejercito_enemigo.cargar_gatos(archivo_dificultad[int(opcion)-1]))
    ronda = ejercito_enemigo.crear_ronda(rondas_faltantes)
    tropas_disponibles = ejercito_aliado.cargar_gatos('unidades')
    mago_disponibles = []
    guerreros_disponibles = []
    caballeros_disponibles =[]

    for tropa in tropas_disponibles:
        if 'GUE' in tropa[0]:
            guerreros_disponibles.append(tropa)
        if 'MAG' in tropa[0]:
            mago_disponibles.append(tropa)
        if 'CAB' in tropa[0]:
            caballeros_disponibles.append(tropa)

    while not fin_programa:
        opcion = None
        opcion = menu_inicio(ejercito_aliado, opciones, opcion)

        if opcion == '1':
            opcion = None
            while opcion != '0':
                opcion = menu_tienda(ejercito_aliado, opciones, opcion)
                if opcion == '1':
                    if len(mago_disponibles) > 0:
                        if ejercito_aliado._oro >= 11:
                            ejercito_aliado.crear_gato(mago_disponibles)
                            ejercito_aliado._oro -= 11
                            print('Se ha gastado 11 de oro')
                        else:
                            print('No hay suficiente dinero :o')
                    else:
                        print('Compra no disponible :o')

                elif opcion == '2':
                    if len(guerreros_disponibles) > 0:
                        if ejercito_aliado._oro >= 9:
                            ejercito_aliado.crear_gato(guerreros_disponibles)
                            ejercito_aliado._oro -= 9
                            print('Se ha gastado 9 de oro')
                        else:
                            print('No hay suficiente dinero :o')
                    else:
                        print('Compra no disponible :o')

                elif opcion == '3':
                    if len(caballeros_disponibles) > 0:
                        if ejercito_aliado._oro >= 10:
                            ejercito_aliado.crear_gato(caballeros_disponibles)
                            ejercito_aliado._oro -= 10
                            print('Se ha gastado 10 de oro')
                        else:
                            print('No hay suficiente dinero :o')
                    else:
                        print('Compra no disponible :o')

                elif opcion == '4':
                    if ejercito_aliado._oro >= 6 and len(ejercito_aliado.combatientes) > 0:
                        seleccion_gato(ejercito_aliado.combatientes)
                        item = gato.Armadura()
                        item.comprar(ejercito_aliado)
                        while True:
                            opcion = input()
                            if opcion.isdigit():
                                opcion = int(opcion)
                                if 1 <= opcion <= len(ejercito_aliado.combatientes):
                                    break
                            print("Seleccione una opcion valida")
                        gato_evolucionado = ejercito_aliado.combatientes[int(opcion) - 1]
                        if item.aplicar_item(ejercito_aliado, gato_evolucionado) == False:
                            ejercito_aliado._oro += 6
                    else:
                        print('No hay suficientes combatientes/dinero :o')

                elif opcion == '5':
                    if ejercito_aliado._oro >= 7 and len(ejercito_aliado.combatientes) > 0:
                        seleccion_gato(ejercito_aliado.combatientes)
                        item = gato.Pergamino()
                        item.comprar(ejercito_aliado)
                        while True:
                            opcion = input()
                            if opcion.isdigit():
                                opcion = int(opcion)
                                if 1 <= opcion <= len(ejercito_aliado.combatientes):
                                    break
                            print("Seleccione una opcion valida")
                        gato_evolucionado = ejercito_aliado.combatientes[int(opcion) - 1]
                        if item.aplicar_item(ejercito_aliado, gato_evolucionado) == False:
                            ejercito_aliado._oro += 7
                    else:
                        print('No hay suficientes combatientes/dinero :o')

                elif opcion == '6':
                    if ejercito_aliado._oro >= 5 and len(ejercito_aliado.combatientes) > 0:
                        seleccion_gato(ejercito_aliado.combatientes)
                        item = gato.Lanza()
                        item.comprar(ejercito_aliado)
                        while True:
                            opcion = input()
                            if opcion.isdigit():
                                opcion = int(opcion)
                                if 1 <= opcion <= len(ejercito_aliado.combatientes):
                                    break
                            print("Seleccione una opcion valida")
                        gato_evolucionado = ejercito_aliado.combatientes[int(opcion) - 1]
                        if item.aplicar_item(ejercito_aliado, gato_evolucionado) == False:
                            ejercito_aliado._oro += 5
                    else:
                        print('No hay suficientes combatientes/dinero :o')

                elif opcion == '7':
                    if ejercito_aliado._oro >= 7 and len(ejercito_aliado.combatientes) > 0:
                        for gato in ejercito_aliado.combatientes:
                            gato.curarse()
                        print('Todos los combatientes recibieron 35 puntos de vida!!!')
                        ejercito_aliado._oro -= 7
                    else:
                        print('No hay suficientes combatientes/dinero :o')

                elif opcion == '0':
                    print('Regresando al menu principal.')
                continuar(opcion)
            opcion = None

        elif opcion == '2':
            ejercito_aliado.presentarse()
            opcion = None
            continuar(opcion)
        
        elif opcion == '3':
            resultado = ejercito_aliado.combatir(ejercito_enemigo)
            opcion = None
            if resultado == False:
                print(""" 
    Mejor suerte a la proxima :c 
                      """)
            else:
                if len(rondas_faltantes) > 0:
                    ronda = ejercito_enemigo.crear_ronda(rondas_faltantes)
                else:
                    print("""\       
             ___                                               ___ 
            (___)                                             (___)
            |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
            |   |  _____                       _       _ _ _  |   | 
            |   | |  __ \                     | |     | | | | |   | 
            |   | | |  \/ __ _ _ __   __ _ ___| |_ ___| | | | |   | 
            |   | | | __ / _` | '_ \ / _` / __| __/ _ \ | | | |   | 
            |   | | |_\ \ (_| | | | | (_| \__ \ ||  __/_|_|_| |   | 
            |   |  \____/\__,_|_| |_|\__,_|___/\__\___(_|_|_) |   | 
            |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
            (___)                                             (___)

                        """)
                    resultado = False
            continuar(opcion)
            if resultado == False:
                opcion = '0'
        
        if opcion == '0':
            print('          El juego se cerrara, gracias por jugar!!!  ')
            fin_programa = True
