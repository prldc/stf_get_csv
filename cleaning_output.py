import pandas as pd

df = pd.read_json('adi_infos.json')
df = df[['nome', 'data_julgamento', 'data_publicacao', 'Decisão', 'Legislação', 'Observação', 'Ementa', 'partes', 'link', 'Indexação', 'Acórdãos no mesmo sentido', 'Doutrina']]
df["data_julgamento"] = df["data_julgamento"].str.slice(12,).str.strip()
df["data_publicacao"] = df["data_publicacao"].str.slice(12,).str.strip()
df["link"] = df["link"].str.slice(24, -1).str.strip()

missing_names = df[df.nome.isna()]  # save to CSV and scrape missing values.
missing_names.to_csv('missing_names.csv', index=False)
missing_names_scraped = pd.read_json('missing_names_scraped.json')
df = df.dropna(subset=["nome"])
adi_infos_complete = pd.concat([df, missing_names_scraped])
adi_infos_complete.to_csv('adi_infos.csv', index=False)

infos = pd.read_csv('adi_infos.csv')
pdfs = pd.read_csv('adi_pdfs.csv')
adi_combined = pd.merge(infos, pdfs)
adi_combined.to_csv('adi_combined.csv', index=False)