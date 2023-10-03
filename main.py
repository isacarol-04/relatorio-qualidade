import pandas as pd

sitelist = pd.read_excel("SiteList.xlsx")
results = pd.read_excel("Results.xlsx")

colunas_sitelist = sitelist[['Site Name', 'Site ID']]
colunas_results = results[['Site ID', 'Equipment', 'Signal (%)', 'Quality (0-10)', 'Mbps']]

#Separa a informação de Site Name em nome e estado                                         
tempName = colunas_sitelist['Site Name'].str.split('-', expand=True)[1]
colunas_sitelist.drop('Site Name', axis=1, inplace=True)
colunas_sitelist['State'] = tempName.str.slice(start=-2)
colunas_sitelist['Site'] = tempName.str.slice(stop=-2)

#Mescla as colunas/planilhas de acordo com a coluna Site ID
df_relatorio = pd.merge(colunas_sitelist, colunas_results, on='Site ID')

#Organiza as colunas e organiza em ordem alfabetica de acordo com o estado
df_relatorio = df_relatorio[['Site','Site ID', 'State', 'Equipment', 'Signal (%)', 'Quality (0-10)', 'Mbps' ]]
df_relatorio = df_relatorio.sort_values(by='State')

print(df_relatorio)

#Cria arquivo .xlsx com o resultado do relatorio
relatorio_file = "relatorio.xlsx"
df_relatorio.to_excel(relatorio_file, index=False)

#Organiza as colunas
results = results[['City','Site ID', 'State', 'Quality (0-10)', 'Mbps', 'Alerts' ]]

#Muda coluna Yes or No para 1 ou 0
results['Alerts'] = results['Alerts'].map({'Yes': 1, 'No': 0})

print("Site com alarmes ativos: ")
print(results[results['Alerts']==1])

print("\nSites com 0 de Qualidade: ")
print(results[results['Quality (0-10)'] == 0])

print("\nSites com mais de 80 Mbps: ")
print(results[results['Mbps'] > 80])

print("\nSites com menos de 10 Mbps: ")
print(results[results['Mbps'] < 10])

sites_nao_presentes = colunas_sitelist[~colunas_sitelist['Site ID'].isin(colunas_results['Site ID'])]
print("\nSites que nao estao presentes no Results: ")
print(sites_nao_presentes)
