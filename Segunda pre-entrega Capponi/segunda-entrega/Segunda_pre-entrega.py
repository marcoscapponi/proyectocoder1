class Cliente:

    def __init__(self, nombre, mail, fecha, compra, metodoPago):
        
        self.nombre = nombre
        self.mail = mail
        self.fecha = fecha
        self.compra = compra
        self.metodoPago = metodoPago
    
    def __str__(self):
        return f"Cliente: {self.nombre}\n Mail: {self.mail}\n"
    
    def metodo_pago_valido(self, metodo_pago):
        
        metodo_pago = "debito visa"

        if self.metodoPago == metodo_pago:
            print("Metodo valido :)")
        else:
            print("No es posible realizar la compra con este medio. Pruebe otro.")
    
    def costo_total(self, costo):
        self.compra = costo
        print(f"el costo de la compra es de {costo} dolares. ")
    
cliente1 = Cliente("Edgar", "Edgargomez@gmail.com", "20/06/2024", 145, "debito visa")
cliente1.metodo_pago_valido("debito visa")
cliente1.costo_total(145)
print(f"El nombre del cliente es: {cliente1.nombre}")
print(f"la fecha de la compra es: {cliente1.fecha}")
