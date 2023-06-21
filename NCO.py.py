# Bibliotecas com as opções de carbonos, ligações e funções químicas
C = ['met', 'et', 'prop', 'but', 'pent', 'hex', 'hept', 'oct', 'non', 'dec']
Lig = ['an', 'en', 'in', 'dien']
Fun = ['o', 'ol', 'al', 'ona', 'amina', 'óico', 'ano', 'ila', 'enol']

while True:
# Pergunta 1
    while True:
        try:
            num_carb = int(input('Quantos carbonos tem na ligação (1-10)? '))
            if num_carb < 1 or num_carb > 10:
                print('Por favor, insira um número válido entre 1 e 10.')
                continue
            break
        except ValueError:
            print('Por favor, insira um número inteiro válido entre 1 e 10.')

    # Pergunta 2: Qual o tipo de ligação?
    while True:
        try:
            tipo_lig = int(input('Qual o tipo de ligação?\n1 - an\n2 - en\n3 - in\n4 - dien\n'))
            if tipo_lig < 1 or tipo_lig > 4:
                print('Por favor, insira um número válido entre 1 e 4.')
                continue
            break
        except ValueError:
            print('Por favor, insira um número inteiro válido entre 1 e 4.')
    
    # Pergunta 3: Qual o tipo de função química?
    while True:
        try:
            tipo_fun = int(input('Qual o tipo de função química?\n1 - Hidrocarboneto\n2 - Álcool\n3 - Aldeído\n4 - Cetona\n5 - Amina\n6 - Ácido carboxílico\n7 - Éter\n8 - Éster\n9 - Enol\n'))
            if tipo_fun < 1 or tipo_fun > 9:
                print('Por favor, insira um número válido entre 1 e 9.')
                continue
    
            if tipo_fun == 1:
              while True:
                try:
                  carbono_ramif = int(input('Em qual carbono há ramificação? '))
                  if carbono_ramif < 1 or carbono_ramif > num_carb:
                    print(f'Por favor, insira um número válido entre 1 e {num_carb}.')
                    continue
                  break
                except ValueError:
                  print(f'Por favor, insira um número inteiro válido entre 1 e {num_carb}.')
    
              nome_comp = C[num_carb-1] + '-' + str(carbono_ramif) + "-" + Lig[tipo_lig-1] + Fun[tipo_fun-1]
            
            elif tipo_fun == 7:
              nome_comp = 'oxi' + C[num_carb-1] + Lig[tipo_lig-1] + 'ano'
    
            elif tipo_fun == 8:
              nome_comp = 'ato' + C[num_carb-1] + Lig[tipo_lig-1] + 'ila'
    
            else:
              nome_comp = C[num_carb-1] + Lig[tipo_lig-1] + Fun[tipo_fun-1]
    
            print('O nome do composto é:', nome_comp)
            break
        except ValueError:
            print('Por favor, insira um número inteiro válido entre 1 e 9.')