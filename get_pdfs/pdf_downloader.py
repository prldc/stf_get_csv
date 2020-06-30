import os
import pandas as pd
import requests

df = pd.read_csv('/Users/pldc/Scrapes/get_csv/adi_links.csv')
# os.mkdir('ADI PDFs')
os.chdir('/Users/pldc/Scrapes/get_csv/get_pdfs/ADI PDFs')

for row in df.iterrows():
    response = requests.get(row[1][2])
    filename = f"{row[1][0]}.pdf"
    with open(filename, 'wb') as f:
        f.write(response.content)