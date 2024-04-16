class Factura:
    def __init__(self, importe):
        self.importe = importe

    def detalle_factura(self):
        return f"Importe total de la factura: ${self.importe}"

class FacturaFactory:
    def crear_factura(self, importe, condicion_impositiva):
        if condicion_impositiva == "IVA Responsable":
            return FacturaIVAResponsable(importe)
        elif condicion_impositiva == "IVA No Inscripto":
            return FacturaIVANoInscripto(importe)
        elif condicion_impositiva == "IVA Exento":
            return FacturaIVAExento(importe)
        else:
            raise ValueError("Condición impositiva no válida")

class FacturaIVAResponsable(Factura):
    def detalle_factura(self):
        return f"Factura con IVA Responsable\n{super().detalle_factura()}"

class FacturaIVANoInscripto(Factura):
    def detalle_factura(self):
        return f"Factura con IVA No Inscripto\n{super().detalle_factura()}"

class FacturaIVAExento(Factura):
    def detalle_factura(self):
        return f"Factura con IVA Exento\n{super().detalle_factura()}"

factory = FacturaFactory()

factura1 = factory.crear_factura(1000, "IVA Responsable")
print(factura1.detalle_factura())

factura2 = factory.crear_factura(1500, "IVA No Inscripto")
print(factura2.detalle_factura())

factura3 = factory.crear_factura(800, "IVA Exento")
print(factura3.detalle_factura())
