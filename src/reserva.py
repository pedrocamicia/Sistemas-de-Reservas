class Reserva:
    def __init__(self, cliente, producto,inicio,fin):
        self.cliente = cliente
        self.producto = producto
        self.inicio = inicio
        self.fin = fin
        self.estado_reserva = Solicitada()


    def validar_reserva(self):
        self.producto.agregar_reserva(self)
        if self.cumple_condiciones():
            self.estado_reserva.confirmar(self)
        else:
            self.invalidar_reserva(self)


    
    def cumple_condiciones(self):
        return self.validar_solapamiento(self.producto.reservas_validas())  #por ahora, luego se agregaran mas
    
        
    def solapamiento_con_una(self, reserva):
        return self.fin < reserva.inicio or self.inicio > reserva.fin
    
    def validar_solapamiento_con_lista(self, reservas):
        return all(self.validar_solapamiento(self,reserva) for reserva in reservas)
    
    
    
        
    def estado_reserva(self):
        return self.estado_reserva
    
    def es_valida(self):
        return self.estado_reserva.es_valida()
    
    
    
    def invalidar_reserva(self):#responde a la regla de negocio una reserva puede dehjar de ser valida sin intervencion del cliente. llamando a este metodo de cualquier clase se la invalida
        self.estado_reserva.invalidar(self)
    
    def consumir_reserva(self):
        self.estado_reserva.finalizar(self)#ver si hay mas consecuencias.
    
    
    
    
class EstadoReserva:
    def es_valida(self):
        return False
    
    def confirmar(self, reserva):
        raise Exception("no se puede confirmar la reserva en el estado de reserva actual")
        
    def invalidar(self, reserva):
        raise Exception("no se puede invalidar en el estado de reserva actual")
        
    def finalizar(self, reserva):
        raise Exception("no se puede finalizar en el estado de reserva actual")
        
    def cancelar(self, reserva):
        reserva.estado_reserva = Cancelada()
        
class Solicitada(EstadoReserva):
    def confirmar(self, reserva):
        reserva.estado_reserva = Valida()
        
    def invalidar(self, reserva):
        reserva.estado_reserva = Rechazada()
                
class Valida(EstadoReserva):
    def es_valida(self):
        return True

    def finalizar(self, reserva):
        reserva.estado_reserva = Finalizada()
        
    def invalidar(self, reserva):
        reserva.estado_reserva = Rechazada()
        
class Rechazada(EstadoReserva):
    
    def cancelar(self, reserva):
        raise Exception("no se puede cancelar la reserva, ya fue finalizada")

class Finalizada(EstadoReserva):
    pass  

class Cancelada(EstadoReserva):
    pass