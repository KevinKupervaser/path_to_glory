def suma(x,y):
    return x + y
def resta(x,y):
    return x - y
def multiplicacion(x,y):
    return x * y
def division(x,y):
    return x / y

print("1.suma")
print("2.resta")
print("3.multiplicacion")
print("4.division")

while True:
    opcion = input("Elegi una opcion para continuar (1/2/3/4): ")
    if opcion in ("1", "2", "3", "4"):
        num1 = float(input("Escribe un numero: "))
        num2 = float(input("Escribi otro numero: "))

        if opcion == "1":
            print(num1, "+", num2, "=", suma(num1,num2))
            break
        elif opcion == "2":
            print(num1, "-", num2, "=", resta(num1,num2))
            break
        elif opcion == "3":
            print(num1, "*", num2, "=", multiplicacion(num1, num2))
            break
        elif opcion == "4":
            print(num1, "/", num2, "=", division(num1,num2))
            break
    else:
        print("input invalid")

