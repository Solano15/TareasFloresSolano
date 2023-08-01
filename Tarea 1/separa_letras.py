# Comprobamos si el parámetro no es un string
if not isinstance(string, str):
    return -100,None, None

# Comprobamos si el string está vacío
if not string.strip():
    return -300,None, None

# Comprobamos si el string solo contiene letras del abecedario
if not string.isalpha():
    return -200,None, None

# Separamos el string en dos: uno con minúsculas y otro con mayúsculas
minusculas = ''.join(char for char in string if char.islower())
mayusculas = ''.join(char for char in string if char.isupper())

return 0,mayusculas,minusculas
