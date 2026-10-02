def salario_triste(salario_bruto):
    impuestos = salario_bruto*0.26
    return salario_bruto-impuestos

print("Hola bebes")
print("Empresa 1")
print(salario_triste(23000))
print("Empresa 2")
print(salario_triste(73000))
print("Empresa 3")
print(salario_triste(18000))
print("=================")

def salario_triste(salario_bruto):
    impuestos = salario_bruto*0.26
    return ((salario_bruto-impuestos)/30)*15

print("Hola bebes")
print("Empresa 1")
print(salario_triste(23000))
print("Empresa 2")
print(salario_triste(73000))
print("Empresa 3")
print(salario_triste(18000))