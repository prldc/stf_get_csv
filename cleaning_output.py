import pandas as pd
#
# df = pd.read_json('adi_infos.json')
# df = df[['nome', 'data_julgamento', 'data_publicacao', 'Decisão', 'Legislação', 'Observação', 'Ementa', 'partes', 'link', 'Indexação', 'Acórdãos no mesmo sentido', 'Doutrina']]
# df["data_julgamento"] = df["data_julgamento"].str.slice(12,).str.strip()
# df["data_publicacao"] = df["data_publicacao"].str.slice(12,).str.strip()
# df["link"] = df["link"].str.slice(24, -1).str.strip()
#
# missing_names = df[df.nome.isna()]  # save to CSV and scrape missing values.
# missing_names.to_csv('missing_names.csv', index=False)
# missing_names_scraped = pd.read_json('missing_names_scraped.json')
# df = df.dropna(subset=["nome"])
# adi_infos_complete = pd.concat([df, missing_names_scraped])
# adi_infos_complete.to_csv('adi_infos.csv', index=False)
#
# infos = pd.read_csv('adi_infos.csv')
# pdfs = pd.read_csv('adi_pdfs.csv')
# adi_combined = pd.merge(infos, pdfs)
# adi_combined.to_csv('adi_combined.csv', index=False)

# df = pd.read_csv('adi_combined.csv')
# df = df.sort_values(by=['nome'])
# combinada = pd.read_csv('combinada.csv')
# comb = pd.read_excel('comb.xlsx')
# comb2 = pd.read_csv('files.csv')
# comb3 = pd.merge(comb, comb2, how = "inner")
# final = pd.concat([combinada, comb3])
# values = {'lista': False}
# final.lista = final.lista.fillna(False)

df = pd.read_csv('planilha_adis.csv')
print(df.lista.loc[df.nome == "ADI 105"])
df.lista.loc[df.nome == "ADI 105"] = True
print(df.lista.loc[df.nome == "ADI 105"])
df.lista.loc[df.nome == "ADI 158"] = True
df.lista.loc[df.nome == "ADI 4807"] = True
df.lista.loc[df.nome == "ADI 5432"] = True
df.lista.loc[df.nome == "ADI 854"] = True
df.lista.loc[df.nome == "ADI 241"] = True
df.lista.loc[df.nome == "ADI 170"] = True