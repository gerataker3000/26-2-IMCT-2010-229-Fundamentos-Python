print(5 <= 3)
print(5 >= 3)
tipo_persona = input("Dime quien eres: ")

if(tipo_persona == "Estudiante"):
    print("Bienvenidos lincesitos")
    # cantidad_avance = int(input("Cantidad de avance: "))
    cantidad_avance = 80
    materias_reprobadas = 0
    print(type(cantidad_avance))
    if(cantidad_avance >= 80 and materias_reprobadas == 0):    
        print("entrar a residencias")
    
elif(tipo_persona == "Maestro"):
    print("Bienvenido maestro")
else:
    print("Eres invitado o algo asi")