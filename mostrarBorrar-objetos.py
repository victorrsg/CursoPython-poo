class Cliente:

   # Cosntructor 
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)
    

class Empresa:
    
    # Constructor
    def __init__(self, clientes=[]):
        self.clientes = clientes
        
    def mostrar_cliente(self, dni=None):
        for cli in self.clientes:
            if cli.dni == dni:
                print(cli)
                return
        print("Cliente no encontrado")
    
    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
                return
        print("Cliente no encontrado")


hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="11111111A")
print(hector)

juan = Cliente("22222222B", "Juan", "Gonzalez Marquez")
print(juan)

empresa = Empresa(clientes=[hector, juan])
empresa.mostrar_cliente("11111111A")
empresa.borrar_cliente("22222222B")

print(empresa.clientes)