from IPython.display import HTML, display
from agents import *
from random import choice


class Food(Thing):
    pass

class Water(Thing):
    pass

class EnergeticBlindDog(Agent):
    location = [0,1]
    direction = Direction("Abajo")
    
    def moveforward(self, success=True):
        '''avanzar solo si es posible si tiene éxito (es decir, ubicación de destino válida)'''
        if not success:
            return
        if self.direction.direction == Direction.R:
            self.location[0] += 1
        elif self.direction.direction == Direction.L:
            self.location[0] -= 1
        elif self.direction.direction == Direction.D:
            self.location[1] += 1
        elif self.direction.direction == Direction.U:
            self.location[1] -= 1
    
    def turn(self, d):
        self.direction = self.direction + d
        
    def eat(self, thing):
        '''devuelve verdadero en caso de éxito o falso de lo contrario'''
        if isinstance(thing, Food):
            return True
        return False
    
    def drink(self, thing):
        ''' devuelve verdadero en caso de éxito o falso de lo contrario'''
        if isinstance(thing, Water):
            return True
        return False
        
def program(percepts):
    '''Devuelve una acción basada en sus percepciones'''
        
    for p in percepts: # primero come o bebe, ¡eres un perro!
        if isinstance(p, Food):
            return 'Comer'
        elif isinstance(p, Water):
            return 'Beber'
        if isinstance(p,Bump): # luego verifique si está al borde y tiene que girar
            turn = False
            choice = random.choice((1,2))
        else:
            choice = random.choice((1,2,3,4)) # 1-derecha, 2-izquierda, otros-adelante
    if choice == 1:
        return 'GiroDerecha'
    elif choice == 2:
        return 'GiroIzquierda'
    else:
        return 'MoverseAdelante'

class Park2D(GraphicEnvironment):
    def percept(self, agent):
        '''devolver una lista de cosas que están en la ubicación de nuestro agente'''
        things = self.list_things_at(agent.location)
        loc = copy.deepcopy(agent.location) # averiguar la ubicación de destino
        #Verifique si el agente está a punto de chocar contra una pared
        if agent.direction.direction == Direction.R:
            loc[0] += 1
        elif agent.direction.direction == Direction.L:
            loc[0] -= 1
        elif agent.direction.direction == Direction.D:
            loc[1] += 1
        elif agent.direction.direction == Direction.U:
            loc[1] -= 1
        if not self.is_inbounds(loc):
            things.append(Bump())
        return things
    
    def execute_action(self, agent, action):
        '''cambia el estado del entorno en función de lo que hace el agente.'''
        if action == 'GiroDerecha':
            print('Nuestro AGENTE ha decidido realizar {} e ir a el lugar: {}'.format( action, agent.location))
            agent.turn(Direction.R)
        elif action == 'GiroIzquierda':
            print('Nuestro AGENTE ha decidido realizar {} e ir a el lugar: {}'.format( action, agent.location))
            agent.turn(Direction.L)
        elif action == 'MoverseAdelante':
            print('Nuestro AGENTE ha decidido moverse a {} en el lugar: {}'.format( agent.direction.direction, agent.location))
            agent.moveforward()
        elif action == "Comer":
            items = self.list_things_at(agent.location, tclass=Food)
            if len(items) != 0:
                if agent.eat(items[0]):
                    print('Nuestro AGENTE comio {} en el lugar: {}'.format( str(items[0])[1:-1], agent.location))
                    self.delete_thing(items[0])
        elif action == "Beber":
            items = self.list_things_at(agent.location, tclass=Water)
            if len(items) != 0:
                if agent.drink(items[0]):
                    print('Nuestro AGENTE bebio {} en el lugar: {}'.format( str(items[0])[1:-1], agent.location))
                    self.delete_thing(items[0])
                    
    def is_done(self):
        '''De forma predeterminada, terminamos cuando no podemos encontrar un agente en vivo,
        pero para evitar matar a nuestro lindo perro, nos detendremos antes de sí mismo, cuando no haya más comida o agua'''
        no_edibles = not any(isinstance(thing, Food) or isinstance(thing, Water) for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)
        return dead_agents or no_edibles

park = Park2D(5,5, color={'EnergeticBlindDog': (200,0,0), 'Water': (0, 200, 200), 'Food': (500, 115, 40)})
dog = EnergeticBlindDog(program)
dogfood = Food()
water = Water()
park.add_thing(dog, [0,0])
park.add_thing(dogfood, [1,2]) #definimos ubicación de comida.
park.add_thing(water, [0,1])#definimos ubicación de Agua.
morewater = Water()
morefood = Food()
park.add_thing(morewater, [2,4]) #definimos ubicación de Agua.
park.add_thing(morefood, [4,3]) #definimos ubicación de comida.
morewater = Water()
morefood = Food()
park.add_thing(morewater, [5,4])#definimos ubicación de Agua.
park.add_thing(morefood, [6,3]) #definimos ubicación de comida.
print("el perro comenzo en [0,0], mirando hacia abajo. ¡¡¡A ver si encuentra comida o agua!!!")
park.run(100) #Definimos la cantidad de pasos que deseamos que realice nuestro agente.

