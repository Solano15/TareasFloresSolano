
def  separa_letras(string ):
    # Comprobamos si el parámetro no es un string
    if not isinstance(string, str):
        return -100, None, None
    
    # Comprobamos si el string está vacío
    if not string.strip():
        return -300, None, None

    # Comprobamos si el string solo contiene letras del abecedario
    if not string.isalpha():
        return -200, None, None

    # Separamos el string en dos: uno con minúsculas y otro con mayúsculas
    minusculas = ''.join(char for char in string if char.islower())
    mayusculas = ''.join(char for char in string if char.isupper())

    return 0, mayusculas, minusculas


def potencia_manual(base, potencia):
    # Verificamos que base y exponente no sean strings
    if isinstance(base, str) or isinstance(potencia, str):
        return -400, None

    # Caso especial: exponente es cero, la potencia es siempre 1
    if potencia == 0:
        return 0, 1

    # Inicializamos el resultado en 1, ya que cualquier número elevado a 0 es 1
    resultado = 1

    # Calculamos la potencia usando sumas y un ciclo for
    for i in range(potencia):
        suma = 0
        for j in range(base):
            suma += resultado
        resultado = suma

    return 0, resultado
