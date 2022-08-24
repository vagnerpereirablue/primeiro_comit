
import requests
import pandas as pd
from datetime import datetime
import time
from openpyxl import Workbook
import requests
import pandas as pd
from datetime import datetime
import time
import csv
import shutil
import pathlib
from pathlib import Path 
from csv import DictReader
import datetime as dt
import csv



#while True:
for i in range(3):    
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()
    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"] 

    tabela = pd.DataFrame(requisicao)
    tabela.loc[0,"Cotacao"] = float(cotacao_dolar)
    tabela.loc[1,"Cotacao"] = float(cotacao_euro)
    tabela.loc[2,"Cotacao"] = float(cotacao_btc) * 1000
    tabela.loc[0,"Data Atual"] = datetime.now()

     
    tabela.to_csv(r"C:\Users\BlueShift\OneDrive - blueshift.com.br\Área de Trabalho\Funcion_teste\dados\2022\7\25\Cotacao.csv",index = False )
    #with open(r'Dados_Cotação\2022\8\12\Cotacao.csv', 'a') as arquivo:
     #   for dia in tabela:
      #      arquivo.write(str(dia)+ '\n')

#dados_teste = pd.DataFrame(lista)
#dados_teste.to_csv(r"C:\Users\BlueShift\OneDrive - blueshift.com.br\Área de Trabalho\Funcion_teste\dados\2022\7\25\Atividades_reportadas.csv")
    with open(r"C:\Users\BlueShift\OneDrive - blueshift.com.br\Área de Trabalho\Funcion_teste\dados\2022\7\25\Cotacao.csv",'a')as arquivo:
        for dia in tabela:
            arquivo.write(str(dia)+ '\n')

            print(f"Cotacao Atualizada. {datetime.now()}")

    time.sleep(180)