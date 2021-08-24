


class Auto():


    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
    
    def moverse(self):
        print(f'el auto {self.__marca} se mueve')
    
    def mostrar_modelo(self):
        print(f'el auto es de modelo {self.__modelo}')

    def set_marca(self, nueva_marca: str):
        if(isinstance(nueva_marca, str)):
            self.__marca = nueva_marca
        else:
            print('la marca debe ser tipo string')
    
    def get_marca(self):
        return self.__marca


auto = Auto('Fiatt', 2000)
auto1 = Auto('Fordd', 2000)


# print(auto.marca, auto.modelo)
# print(auto1.marca, auto1.modelo)

print(auto == auto1)

print(auto)
print(auto1)

auto.moverse()

auto.mostrar_modelo()

# auto.
auto1.set_marca('Ford')
auto1.moverse()
print(auto1.get_marca())
