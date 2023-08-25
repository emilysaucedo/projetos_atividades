#QUESTÃO 2 de 4 - Conteúdo até aula 04
#Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma sorveteria. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
#A Sorveteria possui seguinte relação:

#•	1 bola de sorvete no sabor tradicional (tr) custa 6 reais, no sabor premium (pr) 7 reais e no especial (es) 8 reais;
#•	2 bolas de sorvete no sabor tradicional (tr) custam 11 reais, no sabor premium (pr) 13 reais e no especial (es) 15 reais;
#•	3 bolas de sorvete no sabor tradicional (tr) custam 15 reais, no sabor premium (pr) 18 reais e no especial (es) 21 reais;

#Elabore um programa em Python que:

#A.	Realizar o print uma mensagem de boas-vindas que apareça o seu nome;  
#B.	Deve-se entrar com o sabor (tr/pr/es) e o número de bolas de sorvete desejado (1/2/3) [EXIGÊNCIA DE CÓDIGO 1 de 6];
#C.	Deve-se executar o print da mensagem de “Quantidade de Bolas de Sorvete Inválida". Se o usuário entrar com a quantidade de bolas de sorvete diferente de 1,2 e 3 repetir a partir do item B [EXIGÊNCIA DE CÓDIGO 2 de 6];
#D.	Deve-se executar o print da mensagem de “Sabor de Sorvete Inválido" se o usuário entrar com um sabor diferente de tr (tradicional), pr (premium) e es (especial). Printar: e repetir a partir do item B; [EXIGÊNCIA DE CÓDIGO 3 de 6];
#E.	Deve-se perguntar se o cliente quer pedir mais alguma coisa. Se sim repetir a partir do item B, senão encerrar o programa printando o valor total [EXIGÊNCIA DE CÓDIGO 4 de 6];
#F.	Deve-se utilizar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];
#G.	Deve-se fazer comentários no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
#H.	Deve-se colocar na apresentação de saída de console um pedido no qual o usuário errou ao digitar o sabor do sorvete [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 3];
#I.	Deve-se colocar na apresentação de saída de console um pedido no qual o usuário errou ao digitar o número de bolas de sorvete [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 3];
#J.	Deve-se colocar na apresentação de saída de console um pedido com duas opções sabores diferentes com quantidade de bolas diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 3];  

print('Bem-vinda a Sorveteria da Emily Saucedo Pires')
print('-'*50)

#Apresentando o cardápio da sorveteria
print('-'*50+'Cardápio da Sorveteria'+'-'*50)
print('N° de Bolas'+' '*10+'Sabor Tradicional(tr)'+' '*10+'Sabor Premium(pr)'+' '*10+'Sabor Especial(es)')
print(' '*5+'1'+' '*20+'R$6,00'+' '*22+'R$7,00'+' '*21+'R$8,00')
print(' '*5+'2'+' '*20+'R$11,00'+' '*21+'R$13,00'+' '*20+'R$15,00')
print(' '*5+'3'+' '*20+'R$15,00'+' '*21+'R$18,00'+' '*20+'R$21,00')


total = 0
#Looping para quando a resposta for 's', o programa repete as informações para retirar o pedido até o usuário sair
while True:
  sabor = input('Qual o sabor do sorvete escolhido: (tr/pr/es)').lower()
  while sabor != 'tr' and sabor != 'pr' and sabor != 'es':
    print('Sabor de Sorvete Inválido.')
    sabor = input('Qual o sabor do sorvete escolhido: (tr/pr/es)').lower()
  print('O sabor escolhido foi: ' + sabor)

  bolas = int(input('Quantas bolas de sorvete serão pedidas?'))
  while bolas != 1 and bolas != 2 and bolas != 3:
    print('Quantidade de Bolas de Sorvete Inválida.')
    bolas = int(input('Quantas bolas de sorvete serão pedidas?'))
  print('Foram escolhidas {} bolas do sabor {}.\n' .format(bolas, sabor))

  if sabor == 'tr' and bolas == 1:
    valor2 = 6.00
  elif sabor == 'tr' and bolas == 2:
    valor2 = 11.00
  elif sabor == 'tr' and bolas == 3:
    valor2 = 15.00
  elif sabor == 'pr' and bolas == 1:
    valor2 = 7.00
  elif sabor == 'pr' and bolas == 2:
    valor2 = 13.00
  elif sabor == 'pr' and bolas == 3:
    valor2 = 18.00
  elif sabor == 'es' and bolas == 1:
    valor2 = 8.00
  elif sabor == 'es' and bolas == 2:
    valor2 = 15.00
  else:
    valor2 = 21.00

  total += valor2 #Atribui valor ao pedido, independente do número de vezes que ele acrescente pedidos
  resp = input('Você deseja pedir mais alguma coisa? \n S ou N: ').lower()
  while resp != 's' and resp != 'n':
    print('Resposta inválida.')
    resp = input('Você deseja pedir mais alguma coisa? \nS ou N: ').lower()

  if resp == 'n':
    break

print('\nO valor total do pedido foi de: R${:.2f}' .format(total))