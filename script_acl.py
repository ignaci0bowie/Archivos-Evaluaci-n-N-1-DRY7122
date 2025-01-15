#script: verificar_acl.py

def verificar_acl():

# Solicitar al usuario que introduzca el número de ACL
    try:
        numero_acl = int(input("Introduzca el numero de ACL IPv4: "))

# Determinar el tipo de ACL
        if 1 <= numero_acl <= 99:
            print(f"La ACL numero {numero_acl} es una ACL Estandar.")
        elif 100 <= numero_acl <= 199:
            print(f"La ACL numero {numero_acl} es una ACL Extendida.")
        else:
            print(f"El numero {numero_acl} ingresado no conforma ninguna lista de acceso valida.")
    except ValueError:
        print("Por favor, introduzca un número de lista ACL que sea valida.")

# Punto de entrada del script
if __name__ == "__main__":
    verificar_acl()
