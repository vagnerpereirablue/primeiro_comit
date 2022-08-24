
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
from datetime import datetime, timedelta 


for i in range(30): 
    def geracao_de_dados_todas_as_variaveis(a, b):
        #dia = datetime.today() - timedelta(days= 11)
        CRM73552 = []
        randon_Date = datetime.now()   #(str(dia.day)+ '/' +str(dia.month)+ '/' + str(dia.year))              
        random_value = [61.9, 62.3, 68.4, 69.3]
        random_temp = [26.0, 29.0]
        random_presao = [0.8, 1.7]
        for i in range(a, b):
            CRM73552.append({
                    "Date" : randon_Date,
                    'humid': random.choice(random_value),
                    "temp" : random.choice(random_temp),
                    "presao": random.uniform(7,9),
                    "vazao" : random.choice(random_presao)
                }
                )

        header = ['Date','humid','temp', 'presao', 'vazao']
        file_name = datetime.now().strftime('dados_fakes') + ".csv"

        with open( file_name, 'a',newline="") as csvfile: 
            writer = csv.DictWriter(csvfile, fieldnames = header) 
            writer.writeheader() 
            writer.writerows(CRM73552)

        df = pd.read_csv(r'C:\Users\BlueShift\OneDrive - blueshift.com.br\Área de Trabalho\Dp_300\dados_fakes.csv')    

        return df     
    
    r = geracao_de_dados_todas_as_variaveis(0,50)
    #print(r)
    time.sleep(90)    
