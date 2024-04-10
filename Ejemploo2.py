def calcular(primerNumero, segundoNumero, tercerNumero):
    respuesta = primerNumero * segundoNumero + tercerNumero
    return respuesta

def principal():
    x = 5
    y = 3
    z = 7
    resultado = calcular(x, y, z)
    print("El resultado es:", resultado)

principal()
