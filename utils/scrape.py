import requests
from lxml.html import fromstring
from functools import cache

#Daqui uns 1 mes já vai estar falhando essa porra...
def request_clas_setorial():

    url = 'https://www.b3.com.br/data/files/57/E6/AA/A1/68C7781064456178AC094EA8/ClassifSetorial.zip'
    zip = requests.get(url)

    return zip


@cache
def request_data(ano):
    import zipfile
    import io

    url_base = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'
    page = requests.get(url_base)
    tree = fromstring(page.text)

    hashmap = {(i+2008):i for i in range(2,30)}
    elements = tree.xpath('/html/body/div[1]/pre/a['+ str(hashmap[ano]) +']')

    end_portion_link = elements[0].get('href')

    data = requests.get(url_base + end_portion_link)
    zip = zipfile.ZipFile(io.BytesIO(data.content))

    return zip

#List referente ao link de download de todas companhias   ## ESSA FUNÇÃO NÃO É MAIS USADA PQ BAIXAR O ARQUIVO COM TODAS DFP É MAIS /
# EFICIENTE QUE ACESSAR CADA DFP AVULSA PARA CADA COMPANHIA.
def get_df_list(ano):
    import pandas as pd

    zip = request_data(ano)
    
    arquivo = 'dfp_cia_aberta_' + str(ano) + '.csv'
    content = zip.open(arquivo)
    lines = content.readlines()

    newlines = [line.strip().decode('ISO-8859-1') for line in lines]
    newlines = [line.split(';') for line in newlines]
    df = pd.DataFrame(newlines[1:], columns= newlines[0])

    droplist = ["VERSAO", "CD_CVM","CATEG_DOC", "ID_DOC","ID_DOC"]

    df.drop(columns= droplist, inplace = True)
    sortlist = ["DENOM_CIA", "DT_RECEB"]

    df.sort_values(sortlist, inplace=True)
    new_df = pd.DataFrame(columns=df.columns)
    return_list = ["CNPJ_CIA","DENOM_CIA", "LINK_DOC"]
    for i in range(0,len(df)-1):
        if df.iloc[i]["DENOM_CIA"] == df.iloc[i+1]["DENOM_CIA"]:
            continue
        new_df.loc[len(new_df)] = df.iloc[i]
    
    #retorna o dataframe com o cnpj, nome, e link de download dos demonstrativos financeiros de cada empresa
    return new_df.loc[:,return_list]



