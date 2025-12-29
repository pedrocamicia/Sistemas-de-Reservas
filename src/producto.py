class Producto: 
    def __init__(self):
        self.historial_reservas = HistorialReservas()

    def reservas_validas(self):
        return self.historial_reservas.validas()

    def agregar_reserva(self, reserva):
        self.historial_reservas.agregar(reserva)



class Vehiculo(Producto):
    pass


class HistorialReservas():
    def __init__(self):
        self.reservas =[]
        
    def validas(self):
        return self.reservas.filter(lambda reserva: reserva.es_valida(), self.reservas)
    
    def agregar(self,reserva):
        self.reservas.append(reserva)