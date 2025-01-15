#script solicitar_informacion.py

def solicitar_informacion():
    print("Por favor, ingresa la siguiente información:")

#solicitar información al usuario
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    codigo_seccion = input("Código-Sección: ")
    sede = input("Sede: ")
    
    # Mostrar la información ingresada
    print("Información ingresada:")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Código-Sección: {codigo_seccion}")
    print(f"Sede: {sede}")

# Punto de entrada del script
if __name__ == "__main__":
    solicitar_informacion()
