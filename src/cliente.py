from src.reserva import Reserva

class Cliente:
    def __init__(self, id_cliente, nombre):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.historial_reserva = HistorialReserva()
        
    def solicitar_reserva(self, producto, inicio, fin):
        reserva = Reserva(self,producto, inicio, fin)
        if self.solicitud_compatible(reserva):
            self.historial_reservas.agregar_reserva(reserva)
            reserva.validar_reserva() 
        
    def solicitud_compatible(self, reserva):
        return reserva.validar_solapamiento_con_lista(self.historial_reserva.reservas_historicas)
            
            
    def acceder_a_reserva(self, reserva): #o ver si debe ingresar el recurso, y el historial chequea si hay una reserva para este recurso 
        if self.historial_reserva.existe_reserva(reserva):
            reserva.consumir_reserva()        #ver aca tema de si la reserva ingresada por parametro es la misma que la del historial. es decir si se llama al mismo objeto o si el historial teien q retornarlo para manipularlo a el diretamente
        else:
            print("no existe la reserva")
    
    def cancelar_reserva(self, reserva):
        if self.historial_reserva.existe_reserva(reserva):
            reserva.cancelar()
        else:
            print("no existe la reserva")

class HistorialReserva:
    def __init__(self):
        self.reservas_historicas = []
        
    def agregar_reserva(self,reserva):
        self.reservas_historicas.append(reserva)
    
    def existe_reserva(self, reserva):
        return reserva in self.reservas_historicas
        
        

