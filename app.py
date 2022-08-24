
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


print("Data atual: " + str(dt.date.today()))

data_completa = dt.datetime.now()
#declaração das variavéis
ano = data_completa.year
mes = data_completa.month
dia = data_completa.day
print("Ano " + str(ano) + ", mes " + str(mes) + " e dia " + str(dia))
#caminho da fonte
caminho_base = "Dados_Cotação"
caminho_ano = caminho_base + "/" + str(ano)
caminho_mes = caminho_ano + "/" + str(mes)
caminho_dia = caminho_mes + "/" + str(dia)
# Cria pasta do Ano
Path(caminho_ano).mkdir(parents=True, exist_ok=True)
# Cria pasta do mes
Path(caminho_mes).mkdir(parents=True, exist_ok=True)
# Cria pasta do dia
Path(caminho_dia).mkdir(parents=True, exist_ok=True)
lista = ['dia 1','dia 2','dia 3','dia 4','dia 5']
with open(r'C:\Users\BlueShift\OneDrive - blueshift.com.br\Área de Trabalho\Dp_300\Dados_Cotação\lista dias.csv', 'a') as arquivo:
    for dia in lista:
        arquivo.write(str(dia)+ '\n')


