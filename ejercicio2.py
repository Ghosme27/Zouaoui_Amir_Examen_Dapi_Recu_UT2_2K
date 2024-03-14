consumo_diario = {}
Alimento = input('Ingrese el nombre del alimento:')
Gramos = input('Ingrese la cantidad consumida:')
consumo_diario[Alimento] = Gramos
c = input('¿Quieres registrar otro alimento?(Si/No)')
while True:
    
    if c.lower() == 'si':
        Alimento = input('Ingrese el nombre del alimento:')
        Gramos = input('Ingrese la cantidad consumida:')
        c = input('¿Quieres registrar otro alimento?(Si/No)')
        consumo_diario[Alimento] = Gramos
    else:
        print('Resumen del consumo diario:')
        print(consumo_diario)
        break

