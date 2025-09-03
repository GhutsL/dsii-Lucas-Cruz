media = float(input('Digite a media do aluno: '))
if media >= 5:
    #print('A media informada é: ',media, 'Aluno foi aprovado')
    print(f'A media informada é: {media} Aluno foi aprovado')
elif  media >= 4 and media <= 4.9:
    print('A media informada é :',media, 'Aluno ficou de recuperação')
else:
    print('A media informado é: ',media, 'Aluno foi reprovado')