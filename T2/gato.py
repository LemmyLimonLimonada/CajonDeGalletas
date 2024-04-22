from abc import ABC, abstractmethod
from random import random
import parametros as stat
import os


class Ejercito:
    def __init__(self):
        self.combatientes = []
        self._oro = 35
        self.ronda = 1

    @property
    def oro(self):
        return self._oro
    
    @oro.setter
    def oro(self, p):
        if p <= 0:
            self._oro = 0
        else:
            self._oro = p

    def combatir(self, enemigo):
        aliado = self.combatientes
        rival = enemigo.combatientes

        while len(aliado) != 0 and len(rival) != 0:
            print(f"""\
                  
        *** Combatiente:{rival[0].nombre} de tipo {rival[0].clase}, peleen!!! ***
                            """)
            peleador = aliado[0]
            contrincante = rival[0]
            combate = True


            while combate:
                dmg1 = peleador.atacar(contrincante)
                dmg2 = contrincante.atacar(peleador)
                print(f'{peleador.nombre} ataco a {contrincante.nombre} e hizo {round(dmg1)} de daño.')
                print(f'{contrincante.nombre} ataco a {peleador.nombre} e hizo {round(dmg2)} de daño.')
                contrincante.vida -= dmg1
                peleador.vida -= dmg2
                print(f'A {contrincante.nombre} le queda {round(contrincante._vida)} puntos de vida!')
                print(f'A {peleador.nombre} le queda {round(peleador._vida)} puntos de vida!')
                
                if peleador._vida <= 0 or contrincante._vida <= 0:
                    combate = False

        if len(aliado) > len(rival):
            self._oro += 30
            self.ronda += 1
            print(f"""
                            
        *** Termino el combate!!! ***
            Ganaste!!!
                    Oro total: {self._oro}          """)
            return True
  
        else:
            print(f"""\
                            
        *** Termino el combate!!! ***
            Perdiste :ccc
                                    """)
            return False
    
    def presentarse(self):
        print(f"""
              

    .·:''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''':·.
    : :  ___  _            _ _            _                 _           : :
    : : | __|(_)___ _ _ __(_) |_ ___   __| |___   __ _ __ _| |_ ___ ___ : :
    : : | _| | / -_) '_/ _| |  _/ _ \ / _` / -_) / _` / _` |  _/ _ (_-< : :
    : : |___|/ \___|_| \__|_|\__\___/ \__,_\___| \__, \__,_|\__\___/__/ : :
    : :    |__/                                  |___/                  : :
    '·:.................................................................:·'    
            
                    """)    
        for gato in self.combatientes:
            print(f'{self.combatientes.index(gato) + 1}) {gato}')
        if len(self.combatientes) > 1:
            print(f'Te quedan {len(self.combatientes)} combatientes. ¡Éxito, Guerrero!')
        elif len(self.combatientes) == 1:
            print(f'Te queda 1 combatiente. ¡Éxito, Guerrero!')
        else:
            print('No tienes gatos disponibles :o')

    def cargar_gatos(self,nombre_archivo: str):
        path = 'data/' + str(nombre_archivo) + '.txt'
        gatos_disponibles = []

        if  os.path.exists(path) == False:
                print('Datos corruptos :c')
                print(path)
                return None
        with open(path, 'r') as enemigos:
            datos = enemigos.readlines()
            for linea in datos:
                gatos_disponibles.append(linea.strip('\n').split(';'))
        return gatos_disponibles 
    
    def crear_gato(self, lista):
        if len(lista) > 0:
            gato = lista.pop(0)[0]
            gato = gato.split(',')
            if gato[1] == 'GUE':
                Guerrero(gato[0], int(gato[2]), int(gato[3]), int(gato[4]), int(gato[5]), int(gato[6]), self)
            elif gato[1] == 'MAG':
                Mago(gato[0], int(gato[2]), int(gato[3]), int(gato[4]), int(gato[5]), int(gato[6]), self)
            elif gato[1] == 'CAB':
                Caballero(gato[0], int(gato[2]), int(gato[3]), int(gato[4]), int(gato[5]), int(gato[6]), self)
            print(f'{gato[0]} se ha unido al ejercito!!!')
    
    def crear_ronda(self, lista):
        if len(lista) > 0:
            ronda = lista.pop(0)
            for orden in range(len(ronda)):
                ronda[orden] = ronda[orden].split(',')
            for gato in ronda:
                if gato[1] == 'GUE':
                    Guerrero(gato[0], int(gato[2]), int(gato[3]), int(gato[4]), int(gato[5]), int(gato[6]), self)
                elif gato[1] == 'MAG':
                    Mago(gato[0], int(gato[2]), int(gato[3]), int(gato[4]), int(gato[5]), int(gato[6]), self)
                elif gato[1] == 'CAB':
                    Caballero(gato[0], int(gato[2]), int(gato[3]), int(gato[4]), int(gato[5]), int(gato[6]), self)
                elif gato[1] == 'PAL':
                    Paladin(gato[0], int(gato[2]), int(gato[3]), int(gato[4]), int(gato[5]), int(gato[6]), self)
                elif gato[1] == 'CAR':
                    CaballeroArcano(gato[0], int(gato[2]), int(gato[3]), int(gato[4]), int(gato[5]), int(gato[6]), self)
                elif gato[1] == 'MDB':
                    MagoBatalla(gato[0], int(gato[2]), int(gato[3]), int(gato[4]), int(gato[5]), int(gato[6]), self)
            
class Combatiente(ABC):
    def __init__(self, nombre, vida_max, defensa, poder,  agilidad, resistencia, ejercito) -> None:
        super().__init__()
        self.nombre = nombre
        self.vida_max = vida_max
        self._vida = vida_max
        self._poder = poder
        self._defensa = defensa
        self._agilidad = agilidad
        self._resistencia = resistencia
        self._ataque = int((round(poder + agilidad + resistencia) * (2 * self._vida)/vida_max))
        self.ronda = ejercito.ronda
        self.ejercito = ejercito
        self.clase = None
        ejercito.combatientes.append(self)

    def verificacion(self):
        if not (0 <= self.vida_max <= 100):
            print('Estadistica "vida maxima" invalido. Terminando programa.')
        if not (1 <= self._poder <= 10):
            print('Estadistica "poder" invalido. Terminando programa.')
        if not (1 <= self._defensa <= 20):
            print('Estadistica "poder" invalido. Terminando programa.')
        if not (1 <= self._agilidad <= 10):
            print('Estadistica "agilidad" invalido. Terminando programa.')
        if not (1 <= self._resistencia <= 10):
            print('Estadistica "resistencia" invalido. Terminando programa.')
        return False
    
    def __str__(self) -> str:
        return f'¡Hola! Soy {self.nombre}, un Gato {self.clase} con {round(self._vida)} / {self.vida_max} de vida, {round(self._ataque)} de ataque y {round(self._defensa)} de defensa.'
    
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, p):
        if p > self.vida_max:
            self._vida = self.vida_max
        elif p <= 0:
            self._vida = 0
            self.ejercito.combatientes.remove(self)
            print(f'{self.nombre} a muerto! :c')
        else:
            self._vida = p
            
    def curarse(self):
        self._vida += stat.curar_vida
        if self._vida > self.vida_max:
            self._vida = self.vida_max
    
    @abstractmethod
    def atacar(self):
        pass
    
    @abstractmethod
    def evolucionar(self):
        pass

class Guerrero(Combatiente):
    def __init__(self, nombre, vida_max, defensa, poder, agilidad, resistencia, ejercito) -> None:
        super().__init__(nombre, vida_max, defensa, poder, agilidad, resistencia, ejercito)
        self.precio = 9
        self.clase = 'Guerrero'

    def atacar(self, oponente):
        dano = self.ronda * (self._ataque - oponente._defensa)
        self._agilidad -= self._agilidad * stat.cansancio
        return dano
    
    def evolucionar(self, ejercito, item):
        if isinstance(item, Pergamino):
            gato = MagoBatalla(self.nombre, self.vida_max, self._defensa, self._poder, self._agilidad, self._resistencia, self.ejercito)
            ejercito.combatientes.remove(self)
            print(f'{self.nombre} evoluciono en un Mago de batalla')
            return gato
        elif isinstance(item, Armadura):
            gato = Paladin(self.nombre, self.vida_max, self._defensa, self._poder, self._agilidad, self._resistencia, self.ejercito)
            ejercito.combatientes.remove(self)
            print(f'{self.nombre} evoluciono en un Paladin')
            return gato
        else:
            print('Objeto no permitido')
            return False
        
class Caballero(Combatiente):
    def __init__(self, nombre, vida_max, defensa, poder, agilidad, resistencia, ejercito) -> None:
        super().__init__(nombre, vida_max, defensa, poder, agilidad, resistencia, ejercito)
        self.precio = 10
        self.clase = 'Caballero'

    def atacar(self, oponente):
        if random() < stat.prob_cab:
            oponente._poder -= oponente._poder * stat.red_cab
            dano = self.ronda * (self._ataque * stat.atq_cab - oponente._defensa)
        else:
            dano = self.ronda * (self._ataque - oponente._defensa)
        self._resistencia -= self._resistencia * stat.cansancio
        return dano
    
    def evolucionar(self, ejercito, item):
        if isinstance(item, Pergamino):
            gato = CaballeroArcano(self.nombre, self.vida_max, self._defensa, self._poder, self._agilidad, self._resistencia, self.ejercito)
            ejercito.combatientes.remove(self)
            print(f'{self.nombre} evoluciono en un Caballero Arcano')
            return gato
        elif isinstance(item, Lanza):
            gato = Paladin(self.nombre, self.vida_max, self._defensa, self._poder, self._agilidad, self._resistencia, self.ejercito)
            ejercito.combatientes.remove(self)
            print(f'{self.nombre} evoluciono en un Paladin')
            return gato
        else:
            print('Objeto no permitido')
            return False
        
class Mago(Combatiente):
    def __init__(self, nombre, vida_max, defensa, poder, agilidad, resistencia, ejercito) -> None:
        super().__init__(nombre, vida_max, defensa, poder, agilidad, resistencia, ejercito)
        self.precio = 11
        self.clase = 'Mago'

    def atacar(self, oponente):
        if random() < stat.prob_mag:
            dano = self.ronda * (self._ataque * stat.atq_mag - oponente._defensa * (1 - stat.red_mag))
        else:
            dano = self.ronda * (self._ataque - oponente._defensa)
        self._resistencia -= self._resistencia * stat.cansancio
        self._agilidad -= self._agilidad * stat.cansancio
        return dano
    
    def evolucionar(self, ejercito, item):
        if isinstance(item, Lanza):
            gato = MagoBatalla(self.nombre, self.vida_max, self._defensa, self._poder, self._agilidad, self._resistencia, self.ejercito)
            ejercito.combatientes.remove(self)
            print(f'{self.nombre} evoluciono en un Mago de batalla')
            return gato
        elif isinstance(item, Armadura):
            gato = CaballeroArcano(self.nombre, self.vida_max, self._defensa, self._poder, self._agilidad, self._resistencia, self.ejercito)
            ejercito.combatientes.remove(self)
            print(f'{self.nombre} evoluciono en un Caballero Arcano')
            return gato
        else:
            print('Objeto no permitido')
            return False
        
class Paladin(Guerrero, Caballero):
    def __init__(self, nombre, vida_max, defensa, poder, agilidad, resistencia, ejercito) -> None:
        super().__init__(nombre, vida_max, defensa, poder, agilidad, resistencia, ejercito)
        self.clase = 'Paladin'

    def atacar(self, oponente):
        if random() < stat.prob_pal:
            dano = self.ronda * (self._ataque * stat.atq_cab - oponente._defensa)
        else:
            dano = self.ronda * (self._ataque - oponente._defensa)
        self._resistencia += self._resistencia * stat.aum_pal
        return dano
    
    def evolucionar(self, ejercito, item):
        print('No puedo evolucionar mas!')
        return False
    
class MagoBatalla(Guerrero, Mago):
    def __init__(self, nombre, vida_max, defensa, poder, agilidad, resistencia, ejercito) -> None:
        super().__init__(nombre, vida_max, defensa, poder, agilidad, resistencia, ejercito)
        self.clase = 'MagoBatalla'

    @property
    def defensa(self):
        return self._defensa
    
    def __str__(self) -> str:
        return f'¡Hola! Soy {self.nombre}, un Gato Mago de Batalla con {round(self._vida)} / {self.vida_max} de vida, {round(self._ataque)} de ataque y {round(self._defensa)} de defensa.'
 
    def atacar(self, oponente):
        if random() < stat.prob_mdb:
            dano = self.ronda * (self._ataque * stat.atq_mag - oponente._defensa * (1 - stat.red_mag))
        else:
            dano = self.ronda * (self._ataque - oponente._defensa)
        self._agilidad -= self._agilidad * stat.cansancio
        self._defensa += self._defensa * stat.def_mdb
        if self._defensa > 20:
            self._defensa = 20  #no tengo idea pq el setter que puse antes no hace que esto se regule solo :c
        return dano
    
    def evolucionar(self, ejercito, item):
        print('No puedo evolucionar mas!')
        return False

class CaballeroArcano(Caballero, Mago):
    def __init__(self, nombre, vida_max, defensa, poder, agilidad, resistencia, ejercito) -> None:
        super().__init__(nombre, vida_max, defensa, poder, agilidad, resistencia, ejercito)
        self.clase = 'Caballero Arcano'

    def atacar(self, oponente):
        if random() < stat.prob_car:
            oponente._poder -= oponente._poder * stat.red_cab
            dano = self.ronda * (self._ataque * stat.atq_cab - oponente._defensa)
        else:
            dano = self.ronda * (self._ataque * stat.atq_mag - oponente._defensa * (1 - stat.red_mag))
        self._agilidad += self._agilidad * stat.aum_car
        self._poder += self._poder * stat.aum_car
        self._resistencia -= self._resistencia * stat.cansancio
        return dano
    
    def evolucionar(self, ejercito, item):
        print('No puedo evolucionar mas!')
        return False

class Item(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    
    def aplicar_item(self, ejercito, gato):
        return gato.evolucionar(ejercito, self)
    
    @abstractmethod
    def comprar(self):
        pass

class Pergamino(Item):
    def __init__(self) -> None:
        super().__init__()
        self.nombre = 'Pergamino'
        self.precio = 7

    def __str__(self) -> str:
        return self.nombre

    def comprar(self, ejercito):
        ejercito._oro -= self.precio

class Lanza(Item):
    def __init__(self) -> None:
        super().__init__()
        self.nombre = 'Lanza'
        self.precio = 5

    def __str__(self) -> str:
        return self.nombre
    
    def comprar(self, ejercito):
        ejercito._oro -= self.precio
    
class Armadura(Item):
    def __init__(self) -> None:
        super().__init__()
        self.nombre = 'Armadura'
        self.precio = 6

    def __str__(self) -> str:
        return self.nombre
    
    def comprar(self, ejercito):
        ejercito._oro -= self.precio