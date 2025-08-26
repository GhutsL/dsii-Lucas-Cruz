x = int(input('Informe o ano de nascimento: '))
idade = 2025 - x
if idade >= 18:
    print(f'Voce é maior de idade {idade} anos')
else:
    print(f'Voce é menor de idade {idade} anos')