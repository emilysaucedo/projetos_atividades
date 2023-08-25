#Questão 03 
#Enunciado: Você foi contratado para desenvolver um sistema de cobrança de banho para um petshop. Você ficou com a parte de desenvolver a interface com o funcionário.
#O petshop opera da seguinte maneira:
#•	Para cães com peso menor que 3 kg o valor base é de 40 reais;
#•	Para cães com peso igual ou maior que 3 kg e menor que 10 kg o valor base é de 50 reais;
#•	Para cães com peso igual ou maior que 10 kg e menor que 30kg o valor base é de 60 reais;  
#•	Para cães com peso igual ou maior que 30 kg e menor que 50kg o valor base é de 70 reais;

#	Para cães com pelo curto (c) o multiplicador é 1;
#	Para cães com pelo médio (m) o multiplicador é 1.5;
#	Para cães com pelo longo (l) o multiplicador é 2;

#♦	Para o adicional de cortar unhas (1) do cachorro é cobrado um valor extra de 10 reais;
#♦	Para o adicional de escovar os dentes (2) do cachorro é cobrado um valor extra de 12 reais;
#♦	Para o adicional de limpar as orelhas (3) do cachorro é cobrado um valor extra de 15 reais;
#♦	Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;


#O valor final da conta é calculado da seguinte maneira:

#total = base * multiplicador + extra

#Função cachorro_peso()
def chachorro_peso():
  while True:
    try:
      pesoCachorro = float(input('Qual é o peso do seu cachorro em kg?'))
      if (pesoCachorro < 3):
        return 40
      elif (3 <= pesoCachorro < 10):
        return 50
      elif (10 <= pesoCachorro < 30):
        return 60
      elif (30 <= pesoCachorro < 50):
        return 70
      else: #Validando o intervalo de valores para o peso
        print('Valor acima do permitido, 50kg. Digite novamente.')
    except ValueError: #Validando o erro de valor não númerico
      print('Digite um valor númerico.')
      continue #voltar para o início
#Fim da função cachorro_peso()

#Função cachorro_pelo()
def cachorro_pelo():
  while True:
      peloCachorro = input('Qual é o tipo de pelo do seu cachorro?\nCurto(c)\nMédio(m)\nLongo(l)\n>>').lower().strip()
      if (peloCachorro == 'c'):
        return 1
      elif (peloCachorro == 'm'):
        return 1.5
      elif (peloCachorro == 'l'):
        return 2
      else: #validando a opção entre as três
        print('Opção inválida.')
        continue #voltar para o início
#Fim da função cachorro_pelo()

#Função cachorro_extra()
def cachorro_extra():
  acumulador = 0 #Acumulador para poder selecionar mais de um serviço extra
  while True:
      adicionalCachorro = (input('Você deseja algum adicional:\n' + '1 - Cortar unhas\n' + '2 - Escovar os dentes\n' + '3 - Limpar as orelhas\n' + '0 - Não deseja nenhum adicional\n' + '>>'))
      if (adicionalCachorro == '0'):
        return acumulador
      if (adicionalCachorro == '1'):
        acumulador += 5
        continue
      elif (adicionalCachorro == '2'):
        acumulador += 12
        continue
      elif (adicionalCachorro == '3'):
        acumulador += 15
        continue
      else:
        print('Opção inválida.')
        continue #voltar para o início
#Fim da função cachorro_extra()

#Programa Principal
print('-'*20 + 'Bem-vinda ao Pet-Shop da Emily Saucedo Pires' + '-'*20)
#Função do peso do cachorro
valorbase = chachorro_peso()
print('Para esse peso, o valor de base é :R${}\n' .format(valorbase))
#Função do multiplicador
multiplicador = cachorro_pelo()
print('Para esse tipo de pelo, o multiplicador é: {}\n' .format(multiplicador))
#Função dos serviços extras
adicional = cachorro_extra()
print('O total extra dos adicionais foi: R${}\n' .format(adicional))
#Resultado Final
print('-'*50)
print('O total da compra foi de: R${:.2f}' .format(valorbase*multiplicador+adicional))

