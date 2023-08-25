#QUESTÃO 4 de 4 - Conteúdo até aula 06
#Enunciado: Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerencialme de pessoas. Este software deve ter o seguinte menu e opções:

#1)	Cadastrar Colaborador
#2)	Consultar Colaborador
#1.	Consultar Todos
#2.	Consultar por Id;
#3.	Consultar por Setor;
#4.	Retornar ao menu;
#3)	Remover Colaborador
#4)	Encerrar Programa

#Elabore um programa em Python.

def cadastrar_colaborador(id):
  print('*'*20)
  print('Menu - CADASTRAR Colaborador')
  print('Código do produto: {}' .format(id))
  nome = input('Nome do colaborador:')
  setor = input('Setor do colaborador:')
  salario = float(input('Salário do colaborador: R$'))
  dic_colab = {'id' : id,
               'nome' : nome,
               'setor' : setor,
               'salario' : salario}
  lista_colaboradores.append(dic_colab.copy())

def consultar_colaborador():
  print('*'*20)
  print('Menu - CONSULTAR Colaborador')
  while True:
    print('-'*20)
    opcao_consult = input('Qual opção desejada:\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Setor\n4. Retornar ao Menu\n')
    if opcao_consult == '1':
      print('Consultar Todos os Colaboradores')
      for colab in lista_colaboradores:
        print('-'*20) #colab vai varrer a lista de caloboradores
        for key, value in colab.items():
          print('{} : {}' .format(key, value)) #varrer os itens do dicionário
    elif opcao_consult == '2':
      print('Consultar Colaborador por Id')
      id_desejada = int(input('Código desejado:'))
      for colab in lista_colaboradores:
        if colab['id'] == id_desejada:
          print('-'*20)
          for key, value in colab.items():
            print('{} : {}' .format(key, value)) #varrer os itens do dicionário
    elif opcao_consult == '3':
      print('Consultar Colaborador por Setor')
      setor_desejada = input('Setor desejado:')
      for colab in lista_colaboradores:
        if colab['setor'] == setor_desejada:
          print('-'*20)
          for key, value in colab.items():
            print('{} : {}' .format(key, value)) #varrer os itens do dicionário
    elif opcao_consult == '4':
      return
    else:
      print('Opção inválida. Tente novamente.')
      continue #voltar para o início

def remover_colaborador():
  print('Menu - REMOVER Colaborador')
  remov = int(input('Entre com o código do colaborador a ser removido:'))
  for colab in lista_colaboradores:
    if colab['id'] == remov:
      lista_colaboradores.remove(colab)
      print('Colaborador removido.')

#Var Globais
colaboradores = {}
lista_colaboradores = []
id_global = 0

#Programa Principal
print('-'*20 + 'Bem-vinda ao Gerenciamento de Pessoas da Emily Saucedo Pires' + '-'*20)
while True:
  print('-'*20)
  opcaomenu = input('Qual a opção desejada:\n1. Cadastrar Colaborador\n2. Consultar Colaborador\n3. Remover Colaborador\n4. Encerrar Programa\n >>')
  if opcaomenu == '1':
      id_global += 1
      cadastrar_colaborador(id_global)
  elif opcaomenu == '2':
      consultar_colaborador()
  elif opcaomenu == '3':
      remover_colaborador()
  elif opcaomenu == '4':
      break
  else:
    print('Opção inválida. Tente novamente.')
    continue #voltar para o início