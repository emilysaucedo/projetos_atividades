#QUESTÃO 1 de 4 - Conteúdo até aula 03
#Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maiores por unidade as informações abaixo:

#•	Se quantidade for menor que 200 o desconto será de 0%;
#•	Se quantidade for igual ou maior que 200 e menor que 1000 o desconto será de 5%;
#•	Se quantidade for igual ou maior que 1000 e menor que 2000 o desconto será de 10%;
#•	Se quantidade for igual ou maior que 2000 o desconto será de 15%;

#Elabore um programa em Python que:
#A.	Realizar o print uma mensagem de boas-vindas que apareça o seu nome;
#B.	Deve-se entrar com o valor unitário e quantidade do produto [EXIGÊNCIA DE CÓDIGO 1 de 4];
#C.	Deve-se retornar o valor total sem desconto e o valor total com desconto [EXIGÊNCIA DE CÓDIGO 2 de 4];
#D.	Deve-se utilizar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 3 de 4];  
#E.	Deve-se fazer comentários no código [EXIGÊNCIA DE CÓDIGO 4 de 4];
#F.	Deve-se colocar na apresentação de saída de console um pedido recebendo desconto [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 1]; 

print("Bem-vinda a Loja da Emily Saucedo Pires")
#Definir as váriaveis que receberão os dados de entrada com valor unitário e quantidade do produto
valor_unit = float(input("Qual o valor unitário do produto? R$"))
qtd = int(input("Qual a quantidade do produto?"))

#Estrutura condicional para aplicar o desconto de acordo com a qtdade de produto
if qtd < 200:
    desconto = 0
elif 200 <= qtd < 1000:
    desconto = 0.05
elif 1000 <= qtd < 2000:
    desconto = 0.10
else:
    desconto = 0.15

#Aplicar o cálculo para o desconto do valor total
semdesc = valor_unit*qtd
comdesc = semdesc*(1-desconto)
#Apresentar o valor a ser pago com desconto e sem
print("O valor total sem desconto é: R${:.2f} " .format(semdesc))
print("O valor total com desconto é: R${:.2f}"  .format(comdesc))
