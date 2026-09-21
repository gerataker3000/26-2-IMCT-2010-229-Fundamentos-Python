taquerias = {
    "Taqueria 1": {
        "Nombre": "Tacos toño",
        "Empleados": 5,
        "Precio por taco": 14,
        "Platillos": []
    },
    "Taqueria 2": {
        "Nombre": "Tacos bajito",
        "Empleados": 7,
        "Precio por taco": 15,
        "Platillos": ["Combo 1"]
    },
    "Taqueria 3": "Rey del taco"
}

for taqueria,nombre in taquerias.items():
    print("")
    print("Numero de taqueria",taqueria)
    print(f"Nombre {nombre}")