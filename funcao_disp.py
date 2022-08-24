# criar uma função que retorne os dados de leiuta dos dispositivos
# Passo 1 => fazer a leitura dos dados 
# Passo 2 => tratar os dados que serão analisados 
# Passo 3 => Aplicar metodos de Machine Learning 
# Passo 4 => Aplicar a função que leia e retorne os dados tratados em uma tela? 

# informe o dispositivo a ser analisado ? 
#(criar uma variavel que leia a lista de dispositivos)
# onde esta a lista dos dispositvos ? 
#(pode trazer essa do container controlador)
# criar uma def que faz a leiutura de todos dispositivos e retorna o dispositivo escolhido
#(já tem uma def que retorna lista pode ser adaptada)
# defenir o camninho em que os dados estarão armazenados para ser feito o tratamento e analise de dados
# retorno da informação em que local. 


def analisar_dispositivo():
      CD_DISPOSITIVO =str(input('Digite o dispositivo a ser analisado'))
      return  CD_DISPOSITIVO
escolhido = analisar_dispositivo()
print(f'O dispositivo escolhido foi {escolhido} :')  





#def soma(x,y):
    #return (x+y)

#a = int(input("Primeiro numero: "))
#b = int(input("Segundo numero : "))
#print("Soma: ", soma(a,b))

