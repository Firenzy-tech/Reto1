# reto 1 mision tic

start =True
product = []
descrip = []
product_iva = []
cant_product = []
count = 0
subtotal = 0
iva_suma = 0
total = 0

while start:
    cant_product.append(float(input("Ingresa las unidades del producto")))
    descrip.append(str(input("Ingrese descripción del producto ")))
    product_sub=(float(input("Ingrese el valor unitario del producto ")))
    val = cant_product[count] * product_sub
    product.append(val)

    iva = str(input("Producto con Iva? S para si y N para No").upper())

    if iva == "N":
        product_iva.append(0)

    else:
        valor = product[count] * 0.19
        product_iva.append(valor)

    subtotal = float(subtotal) + (product_sub * cant_product[count])
    iva_suma = float(iva_suma)+product_iva[count]
    total = float(total) + (product_sub * cant_product[count]) + product_iva[count]
    print("Valor actual ", "Subtotal  :", subtotal, "IVa  :", iva_suma , "Total  :", total)
    keep = str(input("Desea continuar registrando más productos Ingrese S para si o N para no").upper())
    count = count + 1
    if keep == "N":
        for i in range(0, len(product)):

            if product_iva[i] > 0:
                message = "Iva Incluido :"
            else:
                message = "PRODUCTO SIN IVA :"

        print("Descripciòn:", descrip[i], " ", "Subtotal", "  ", product[i], " ", message, product_iva[i])
        print("Total a cobrar ", total)
        start = False
else:
    start = True
