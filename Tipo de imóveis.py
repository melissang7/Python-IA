import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv(r'C:\Users\aluno10\Documents\melissa\aula_01_modulo_03\aluguel.csv', sep = ';')
print(dados)

tipo_de_imovel = dados['Tipo']
print(tipo_de_imovel)
print(type(tipo_de_imovel))

tipo_de_imovel.drop_duplicates(inplace=True)
print(tipo_de_imovel)

print(tipo_de_imovel.index)
print(tipo_de_imovel.shape[0])

tipo_de_imovel.index = range(tipo_de_imovel.shape[0])
print(tipo_de_imovel)

grafico = dados[:5]['Valor'] 
#plt.plot(grafico) 
#plt.show()


tipo_de_imovel.to_csv(r'C:\Users\aluno10\Documents\melissa\aula_01_modulo_03\grafico.csv', sep = '*',index=False)