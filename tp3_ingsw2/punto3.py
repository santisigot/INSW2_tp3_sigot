class Hamburguesa:
    def entrega(self):
        pass

class HamburguesaFactory:
    def fabricar_hamburguesa(self, metodo_entrega):
        if metodo_entrega == "mostrador":
            return HamburguesaMostrador()
        elif metodo_entrega == "cliente":
            return HamburguesaCliente()
        elif metodo_entrega == "delivery":
            return HamburguesaDelivery()
        else:
            raise ValueError("Método de entrega no válido")

class HamburguesaMostrador(Hamburguesa):
    def entrega(self):
        print("La hamburguesa está lista para ser retirada en el mostrador.")

class HamburguesaCliente(Hamburguesa):
    def entrega(self):
        print("La hamburguesa está lista para ser retirada por el cliente.")

class HamburguesaDelivery(Hamburguesa):
    def entrega(self):
        print("La hamburguesa está lista para ser entregada por delivery.")

factory = HamburguesaFactory()

hamburguesa_mostrador = factory.fabricar_hamburguesa("mostrador")
hamburguesa_mostrador.entrega()

hamburguesa_cliente = factory.fabricar_hamburguesa("cliente")
hamburguesa_cliente.entrega()

hamburguesa_delivery = factory.fabricar_hamburguesa("delivery")
hamburguesa_delivery.entrega()
