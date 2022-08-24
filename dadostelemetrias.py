import pandas as pd

previsao = pd.read_csv('Previsao.csv')
print('Dados dias anterior:',previsao['VALUE'][0])
print('Dados dias anterior:',previsao['TARGET'][0])

base = pd.read_csv('Hoje.csv')

try:
    amanha = pd.read_csv('Futuro.csv')
    print('Dados atuais: ',amanha['VALUE'])
    base = base.append(amanha[:1],sort=True)
    amanha = amanha.drop(amanha[:1].index,axis=0)
    base.to_csv('Futuro.csv',index=False)
except Exception:
    print('Os dados ainda não foram atualizados')
    pass

base['TARGET'] = base['VALUE'][1:len(base)].reset_index(drop=True)
previsao = base[-10::].drop('TARGET',axis=1)
treino = base.drop(base[-10::].index,axis=0)
treino.loc[treino['TARGET']> treino['VALUE'],'TARGET']= 1
treino.loc[treino['TARGET']!=1, 'TARGET']= 0

y = treino['TARGET']
x = treino.drop('TARGET',axis = 1)

y = treino['TARGET']
x = treino.drop('TARGET',axis = 1)

from sklearn.model_selection import  train_test_split
x_treino , x_teste ,y_treino, y_teste = train_test_split(x,y, test_size=0.4)

from sklearn.ensemble import ExtraTreesClassifier
modelo = ExtraTreesClassifier()
modelo.fit(x_treino,y_treino)

print('Acuracia',modelo.score(x_teste, y_teste))

previsao['TARGET'] = modelo.predict(previsao)
print('Dados dia anterior',previsao['VALUE'][0])

if previsao['TARGET'][0]==1:
    print('Aumentou a carga')
else:
    print('Diminuiu a carga')

previsao.to_csv('Previsao.csv',index=False)   



