def calcular_descuento(monto_total, porcentaje_descuento=1):
    descuento = monto_total * (porcentaje_descuento / 12)
    return descuento

def main():

    # Llamada a la función con solo el monto total de la compra
    print("En la función principal main, se realizan dos llamadas a esta función")
    monto_total_1 = 500.000
    descuento_1 = calcular_descuento(monto_total_1)
    monto_final_1 = monto_total_1 - descuento_1
    print("Monto total de la compra:", monto_total_1)
    print("Porcentaje de descuento aplicado: 12%")
    print("Monto del descuento aplicado:", descuento_1)
    print("Monto final a pagar después del descuento:", monto_final_1)

    print()

    # Llamada a la función con el monto total de la compra y un porcentaje de descuento personalizado

    monto_total_2 = 200.000
    porcentaje_descuento_personalizado =8
    descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_personalizado)
    monto_final_2 = monto_total_2 - descuento_2
    print("Monto total de la compra:", monto_total_2)
    print(f"Porcentaje de descuento aplicado: {porcentaje_descuento_personalizado}%")
    print("Monto del descuento aplicado:", descuento_2)
    print("Monto final a pagar después del descuento:", monto_final_2)

if __name__ == "__main__":
    main()
