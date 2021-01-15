name = input("Dime tu nombre y apellido: ")
name = name.capitalize()
age = input("Dime cuantos años tienes: ")
print("Tu nombre es", name, "y tienes", age, "años de edad")

def nombre(name, age):
    name = input("Dime tu nombre y apellido: ")
    age = input("Dime cuantos años tienes: ")

while True:
    opcion = input("Son correctos estos datos(si/no): ")
    if opcion in ("si", "no"):
        if opcion == "si":
            city = input("Donde vives: ")
            city = city.capitalize()
            estudias = input("Eres estudiante(si/no): ")
            if estudias in ("si", "no"):
                if estudias == "si":
                    estudias2 = input("Que estudias: ")
                    estudias2 = estudias2.capitalize()
                    print("Tu nombre es", name, "tienes", age,
                          "años de edad,", "vives en", city, "y estudias", estudias2, end=".")
                    break
                if estudias == "no":
                    print("Tu nombre es", name, "tienes", age,
                          "años de edad," "y vives en", city, end=".")
                    break
        elif opcion == "no":
            print(nombre(name, age))



