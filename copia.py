#!/usr/bin/python3

import requests
import pandas as pd
from datetime import datetime
import time
from prophet import Prophet
import csv 
import numpy as np 
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf
from pylab import rcParams


get_ipython().system('pip install pandas-datareader')

get_ipython().system('pip install yfinance')

yf.pdr_override()

#rcParams['figure.figsize'] =  15 , 6

ativos = ['PETR4.SA','ITUB4.SA','MGLU3F.SA']

print(preço)

close = preço["Adj Close"]

close.head(10)

df = pd.DataFrame(close) # transformando em Dataframe
type(df) 

df.index # necessario resetar o index que nesse caso e a data. 

df.reset_index('Date',inplace=True)# Função implace pandas e para fixar a alteração no indice do Dataframe

df.columns = ['ds','y'] # Para trabalhar com o Profhet precisa que as colunas sejam (d e y)
#df.head(10)
df.dtypes

modelo =Prophet()
modelo.fit(df)

data_futuro = pd.date_range(start='2022-08-12', end= '2022-08-31') # fazendo uma previsao futura com um espaço de data usando a ultima leitura disponivel.

type(data_futuro)

df1=pd.DataFrame(data_futuro)

df1.columns = ['ds']

previsao = modelo.predict(df1)
previsao [['ds','yhat','yhat_lower','yhat_upper']]

## 



from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df_treino , df_teste = train_test_split(df,test_size=0.3,shuffle=True)

df_teste

df_treino

modelo2 = Prophet()

modelo2.fit(df_treino)

previsao2 = modelo2.predict(pd.DataFrame(df_teste['ds']))

previsao2.head(5)['yhat']

y_prev = previsao2['yhat'].values
y_true = df_teste['y'].values

mean_squared_error(y_prev,y_true)

