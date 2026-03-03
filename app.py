

print("=== Validación de usuario ===\n")


correo = input("Ingrese su correo: ")

patron_correo = r"^[^@]+@[^@]+\.[^@]+$"

if re.match(patron_correo, correo):
    print("Correo válido ✅\n")
else:
    print("Correo inválido ❌")
    print("Debe tener texto antes y después del '@' y un punto después del '@'\n")
    
contraseña = input("Ingrese una contraseña: ")

tiene_longitud = len(contraseña) >= 8
tiene_mayuscula = bool(re.search(r"[A-Z]", contraseña))
tiene_minuscula = bool(re.search(r"[a-z]", contraseña))
tiene_numero = bool(re.search(r"[0-9]", contraseña))
tiene_especial = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña))

if all([tiene_longitud, tiene_mayuscula, tiene_minuscula, tiene_numero, tiene_especial]):
    print("Contraseña válida ✅")
else:
    print("Contraseña inválida ❌")
    print("Debe cumplir con:")

    if not tiene_longitud:
        print("- Debe tener al menos 8 caracteres")
    if not tiene_mayuscula:
        print("- Al menos una letra mayúscula")
    if not tiene_minuscula:
        print("- Al menos una letra minúscula")
    if not tiene_numero:
        print("- Al menos un número")
    if not tiene_especial:
        print("- Al menos un carácter especial")