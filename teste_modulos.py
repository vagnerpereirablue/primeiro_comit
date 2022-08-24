from pandas._libs.tslibs import period
from pandas.core.indexes.datetimes import date_range
import time
import pandas as pd
from datetime import datetime
import time
import csv
import shutil
import pathlib
from pathlib import Path 
from csv import DictReader
import random

for i in range(100): 
    def geracao_de_dados_todas_as_variaveis(i, f):
        CRM73552 = []
        randon_Date =datetime.now()                     
        random_value = [61.9, 62.3, 68.4, 69.3]
        random_temp = [26.0,45,8,51.7, 63.5]
        random_presao = [15,28,38,88]
        for i in range(i, f):
            CRM73552.append({
                    "Date" : randon_Date,
                    'Bateria': random.choice(random_value),
                    "Latencia" : random.choice(random_temp),
                    "CPU"   : random.choice(random_value),
                    "Memoria"  : random.choice(random_presao)
                }
                )

        header = ['Date','Bateria','Latencia', 'CPU', 'Memoria']
        file_name = datetime.now().strftime('dados_fakes') + ".csv"

        with open( file_name, 'a',newline="") as csvfile: 
            writer = csv.DictWriter(csvfile, fieldnames = header) 
            writer.writeheader() 
            writer.writerows(CRM73552)

        #df = read_csv('/content/dados_fakes.csv')  
        df = pd.read_csv(r'C:\Users\BlueShift\OneDrive - blueshift.com.br\Área de Trabalho\Dp_300\dados_fakes.csv')

        return df     
    
    r = geracao_de_dados_todas_as_variaveis(0,10)
        #print(r)
    time.sleep(90)    


