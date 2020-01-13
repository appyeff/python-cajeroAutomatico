usuarioBD = "yeff"
claveBD = "123456"
saldo = 1000

def validarUsuario(u, c):
    if u == usuarioBD and c == claveBD:
        return True
    return False

def login():
    usuario = input("digite usuario ")
    clave = input("digite contraseña ")
    return validarUsuario(usuario, clave)

def retirar(valor):
    if valor > saldo:
        return False, saldo
    return True, saldo - valor

def depositar(valor):
    return True, saldo + valor

def accion(opcion):
    if opcion == 1:
        valor = int(input("Digite el valor a depositar "))
        return depositar(valor)
    
    if opcion == 2:
        valor = int(input("Digite el valor a retirar "))
        return retirar(valor)
    return False, saldo

def ejecutar():
    if not login():
        print("Usuario o Contraseña inválido")
        return
    
    print("Que desea hacer")
    opcion = int(input("1. Depositar o 2. Retirar "))

    ok, saldo = accion(opcion)
    if not ok:
        print("No se realizo la accion, saldo: ", saldo)
    else:
        print("Accion realizada correctamente, saldo: ", saldo)

ejecutar()

