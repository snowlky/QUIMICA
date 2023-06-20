from termcolor import colored
from tabela import elementos
from cores import cores

# QUIMICA

# Menu:
while True:
  menu = input('''
Insira o número correspondente a opção desejada:
\n1 - Detalhes dos Elementos \n2 - Distribuição Eletrônica \nx - Sair

\n:''')

  
# Detalhes dos Elementos
  
  if menu == "1":
    while True:
      sigla = input(colored('''
-------------------------------------------------------------
DETALHES DOS ELEMENTOS

Insira a sigla do elemento ou 'x' para voltar ao menu principal:
''', "blue"))
      if sigla == "x":
         break
      encontrado = False
      for elemento in elementos:
        if elemento["sigla"] == sigla:
            nome = elemento["nome"]
            simbolo = elemento["sigla"]
            num_atomico = elemento["num_atomico"]
            massa_atomica = elemento["massa"]
            familia = elemento["cor"]
            print("Nome: {}".format(colored(elemento["nome"], elemento["cor"])))
            print("Símbolo: {}".format(simbolo))
            if elemento["cor"] in cores.values():
              print("Número atômico: {}".format(num_atomico))
              print("Massa atômica: {}".format(massa_atomica))
              familia = [key for key, value in cores.items() if value == elemento["cor"]][0]
              print("Família: {}".format(familia))
            encontrado = True
            break
      if not encontrado:
        print(colored('''Elemento não encontrado!
''', "red"))
    
  
# Distribuição Eletronica:
  
  elif menu == "2":
    while True:
      sigla = input(colored('''
-------------------------------------------------------------
DISTRIBUIÇÃO ELETRONICA
      
"Insira a sigla do elemento ou 'x' para voltar ao menu principal: ''', "blue"))
      if sigla == "x":
        break
      encontrado = False
      for elemento in elementos:
        if elemento["sigla"] == sigla:
          num_atomico = elemento["num_atomico"]
          configuracao_eletronica = ""
          prefixos = [
            "1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p",
            "6s", "4f", "5d", "6p", "7s", "5g", "6d", "7p"
          ]
          def maximo_ocupacao(s):
            if s[1] == "s":
              return 2
            elif s[1] == "p":
              return 6
            elif s[1] == "d":
              return 10
            elif s[1] == "f":
              return 14
            else:
              return 14
          for i in range(len(prefixos)):
            max_ocup = maximo_ocupacao(prefixos[i])
            if num_atomico == 0:
              break
            elif num_atomico >= max_ocup:
              configuracao_eletronica += prefixos[i] + str(max_ocup) + " "
              num_atomico -= max_ocup
            elif num_atomico < max_ocup:
              configuracao_eletronica += prefixos[i] + str(num_atomico)
              break
          elemento["distribuicao"] = configuracao_eletronica
          print("Nome: {}".format(colored(elemento["nome"], elemento["cor"])))
          print("Número Átomico ", elemento["num_atomico"])
          print("Distribuição Eletrônica: ", configuracao_eletronica)
          encontrado = True
          break
      if not encontrado:
        print(colored('''Elemento não encontrado!
    ''', "red"))
        
# Fim
  
  elif menu == "x":
    print(colored("Obrigado por usar o programa!    (=^･^=)", "green"))
    break
  else:
    print(colored('''Opção inválida, por favor escolha novamente.
-------------------------------------------------------------''', "red"))
    continue