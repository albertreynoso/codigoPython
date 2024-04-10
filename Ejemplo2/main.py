from Operacion import operacion
if __name__ == '__main__':
 primerNumero = int(input("Ingrese el primer número: "))
 segundoNumero = int(input("Ingrese el segundo número: "))
 tercerNumero = int(input("Ingrese el tercer número: "))

 print(f"{primerNumero} * {segundoNumero} + {tercerNumero} = {operacion(primerNumero,segundoNumero, tercerNumero)}")