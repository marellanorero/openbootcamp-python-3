def imc(peso, estatura):
    """Calcula índice masa corporal"""
    return peso / estatura**2

peso=float(input('Escriba su peso en KG: '))
estatura=float(input('Escriba su estatura en M: '))

indice = imc(peso, estatura)

print('Su IMC es: {}'.format(indice))