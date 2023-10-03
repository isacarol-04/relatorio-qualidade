import pandas as pd

sitelist = pd.read_excel("SiteList.xlsx")
results = pd.read_excel("Results.xlsx")

colunas_sitelist = sitelist[['Site Name']]
colunas_results = results[['Site ID', 'Equipment', 'Signal (%)', 'Quality (0-10', 'Mbps']]

