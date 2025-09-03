idade = int(input('Digite a idade do nadador: '))

if idade >= 5 & idade <= 7:
    print('O nadador é da categoria infatil A')
elif idade <= 11:
    print('O nadador é da categoria infatil B')
elif idade <= 13:
    print('O nadador é da categoria juvenil A')
elif idade <= 17:
    print('O nadador é da categoria juvenil B')
else: 
    print('O nadador é da categoria Adultos')