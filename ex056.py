mediaIdade = somaIdade = homemVelho  = mulherMenosdeVinte = 0
nomeVelho = ''
for pessoa in range (1, 5):
    nome = str(input(f'Digite o nome da {pessoa}ª pessoa: '))
    idade = int(input(f'Digite a idade da {pessoa}ª pessoa: '))
    print(''' Marque seu sexo: 
        [1] Masculino  
        [2] Feminino ''')
    sexo = int(input(f'Assinale o sexo da {pessoa}ª pessoa: '))
    somaIdade += idade
    if pessoa == 1 and sexo == 1:
        homemVelho = idade
        nomeVelho = nome
    if sexo == 1 and idade > homemVelho:
        homemVelho = idade
        nomeVelho = nome    
    else:
        if sexo == 2 and idade < 20:
            mulherMenosdeVinte += 1
            
mediaIdade = somaIdade/4

print(f'A média de idade do grupo é: {mediaIdade}')
print(f'O nome do homem mais velho é: {nomeVelho} e tem: {homemVelho} anos')
print(f'A quantidade de mulher com menos de vinte anos é: {mulherMenosdeVinte}')
        