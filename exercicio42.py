lado1 = float(input('Digite o comprimento do 1 lado do triangulo: '))
lado2 = float(input('Digite o comprimento do 2 lado do triangulo: '))
lado3 = float(input('Digite o comprimento do 3 lado do triangulo: '))

isPossivel = lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2

print('{} possivel formar um triangulo com os comprimentos {},{},{}'.format('E' if isPossivel else 'Nao e',lado1,lado2,lado3))

if(isPossivel):
    if(lado1 == lado2 == lado3):
        print('Triangulo Equilatero')
    elif(lado1 != lado2 != lado3 != lado1):
        print('Triangulo Escaleno')
    else:
        print('Triangulo Isoceles')
