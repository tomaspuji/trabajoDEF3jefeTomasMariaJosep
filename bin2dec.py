
def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    binario = binario[::-1]
    for digito in binario:

        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal