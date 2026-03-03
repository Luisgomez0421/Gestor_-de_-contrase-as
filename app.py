import re

print("Validación de contraseñas\n")

contraseña = input("Ingrese una contraseña: ")

tiene_longitud = len(contraseña) >= 8
tiene_mayuscula = re.search(r"[A-Z]", contraseña)
tiene_minuscula = re.search(r"[a-z]", contraseña)
tiene_numero = re.search(r"[0-9]", contraseña)
tiene_especial = re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña)

if tiene_longitud and tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial:
    print(" Contraseña válida")
else:
    print(" Contraseña inválida")
    print("Debe cumplir con:")

    if not tiene_longitud:
        print(" Debe tener al menos 8 caracteres")
    if not tiene_mayuscula:
        print(" Al menos una letra mayúscula")
    if not tiene_minuscula:
        print(" Al menos una letra minúscula")
    if not tiene_numero:
        print(" Al menos un número")
    if not tiene_especial:
        print(" Al menos un carácter especial")