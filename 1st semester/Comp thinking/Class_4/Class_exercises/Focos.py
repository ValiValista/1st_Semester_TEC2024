"""
Problema 1. Descuentos de mayoreo.

Una tienda mayorista de focos vende únicamente 3 productos, 

foco alógeno luz cálida $250 pesos la caja con 10 piezas, 
foco ahorrador 9w $ 700.00 pesos la caja con 10 piezas y 
foco ahorrador circular 32 w, $1000 pesos la caja con 10 piezas. 

Dependiendo del monto del pedido, la tienda ofrece facilidades de pago de acuerdo con los siguientes rangos. 

Si el cliente compró hasta $5,000, el pago será en una sola exhibición. 
Si compró más de $5000 pero menos de $30000, el pago podrá realizarse a 3 meses sin intereses, 
si compró más de 30000 podrá elegir pago en una sóla exhibición con un 5% de descuento ó un pago a 9 meses sin intereses. 
Tu programa deberá preguntar cuántas cajas de cada producto desea el cliente, 
presentar el monto de compra, 
plantear las opciones de pago, 
y presentar el pago elegido con el monto a pagar 
(en el caso de meses sin intereses o con el 5% de descuento)


Inputs:
    Cajas de cada producto
Outputs:
    Monto de la compra
    Opciones de pago
"""

foco_alo_precio = 250
foco_alo_monto = int(input("Cuantas cajas de focos de alógeno se llevara hoy? \n"))

foco_ahorrador_precio = 700
foco_ahorrador_monto = int(input("Cuantas cajas de focos ahorradores se llevara hoy? \n"))

foco_circular_precio = 1000
foco_circular_monto =  int(input("Cuantas cajas de focos ahorradores circulares se llevara hoy? \n"))

foco_precio_bruto = (foco_alo_precio*foco_alo_monto+foco_ahorrador_monto*foco_ahorrador_precio+foco_circular_monto*foco_circular_precio)
if foco_precio_bruto >0 <5000:
    print(f"Your total for the day is: {foco_precio_bruto}\n")
elif foco_precio_bruto >5000 and foco_precio_bruto<30000:
    msi_3 = input("Would you like to pay in 3 months without interests? Y or N?\n")
    if msi_3 == "Y":
        print(f"Your price would be a total of{foco_precio_bruto} and you would pay {foco_precio_bruto/3} each month\n")
    else:
        print(f"Your price is {foco_precio_bruto}\n")
elif foco_precio_bruto>30000:
    msi_9 = int(input("Would you like a 5""%"" discount or a 9 month without interest purchase: Input 1 or 2 for your option: \n"))
    if msi_9==1:
        print(f"Your total is {foco_precio_bruto}, and you would be paying {foco_precio_bruto/9} per month\n")
    else:
        print(f"Your total with the discount would be {foco_precio_bruto*0.95}\n")
else:
    print("Amount invalid\n")