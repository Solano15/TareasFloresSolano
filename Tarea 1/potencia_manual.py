# Verificamos que base y exponente no sean strings
if isinstance(base, str) or isinstance(potencia, str):
    return -400,None

# Caso especial: exponente es cero, la potencia es siempre 1
if potencia == 0:
    return 0,1
    
# Inicializamos el resultado en 1, ya que cualquier número elevado a 0 es 1
resultado = 1

# Calculamos la potencia usando sumas y un ciclo for
for i in range(potencia):
    suma = 0
    for j in range(base):
        suma += resultado
    resultado = suma

return 0,resultado
