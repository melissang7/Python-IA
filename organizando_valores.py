import pandas as pd

dados = pd.read_csv(r'C:\Users\aluno10\Documents\melissa\aula_01_modulo_03\aluguel.csv', sep = ';')


print(dados)

organizando_valores = dados[['Tipo', 'Bairro', 'Condominio', 'IPTU', 'Valor']]
print(organizando_valores)

organizando_valores.sort_values('Valor', inplace=True, ascending=False)
print(organizando_valores)

organizando_valores = organizando_valores [['Tipo', 'Bairro', 'Valor']]
print(organizando_valores)

organizando_valores.to_csv(r'C:\Users\aluno10\Documents\melissa\aula_01_modulo_03\organizando_valores.csv', sep = ';')