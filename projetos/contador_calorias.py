def converter_metro_cm(altura):
    formatacao_altura = '{:.1f}'.format(altura)
    cm = float(formatacao_altura)*100
    return cm
    
genero = input('Digite H se for homem, digite M se for mulher: ').upper()
print('-'*70)
peso = float(input('Peso em kg: '))
print('-'*70)
altura = float(input('Altura: '))
print('-'*70)
idade = int(input('Idade: '))
print('-'*70)
nivel_de_atividade = input('Níveis de atividade sedentário, pouco ativo, ativo, muito ativo: ')
print('-'*70)

calorias = 0 
calorias_diarias = 0
formatacao_altura = converter_metro_cm(altura)

if altura == float:
    if genero == 'H':
        calorias = (13.75*peso) + (5*formatacao_altura) - (6.76*idade) + 66.5                                                                        
        
    elif genero == 'M':
        calorias = (9.56*peso) + (1.85*formatacao_altura) - (4.68*idade) + 665.4
        
    else:
        print ('Gênero inválido!')
        
else:
    if genero == 'H':
        calorias = (13.75*peso) + (5*altura) - (6.76*idade) + 66.5                                                                        
        
    elif genero == 'M':
        calorias = (9.56*peso) + (1.85*altura) - (4.68*idade) + 665.4
        
    else:
        print ('Gênero inválido!')
 

if nivel_de_atividade == 'sedentário':
    calorias_diarias = calorias * 1.2
    
elif nivel_de_atividade == 'pouco ativo':
    calorias_diarias = calorias * 1.375
    
elif nivel_de_atividade == 'ativo':
    calorias_diarias = calorias * 1.55
    
elif nivel_de_atividade == 'muito ativo':
    calorias_diarias = calorias * 1.725
    
else: 
    print('Nível de ativiade inválido!')
    
print(f'Você deve consumir {calorias_diarias:.2f} por dia.')
print('-'*70)