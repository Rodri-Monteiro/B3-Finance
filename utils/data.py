from functools import cache
from .scrape import (request_data, request_clas_setorial
                    )
import pandas as pd


@cache
def ticker_dict() -> dict:
    arquivo = 'data/tickers.xlsx'
    data = pd.read_excel(arquivo)
    _dict = {}

    cnpj = 'CNPJ_CIA'
    ticker = 'TICKER'

    for i in range(len(data[ticker])):
        data.loc[i,ticker] = list(data.loc[i,ticker].split(','))

    for i in range(len(data[ticker])):
        for j in data.loc[i,ticker]:
            _dict[j] = data.loc[i,cnpj]
    

    return _dict


#Retorna balanço dos ativos da empresa/ano em dataframe
@cache
def get_bs_assets_info(ano)-> pd.DataFrame:
    
    zip = request_data(ano)
    arquivo = 'dfp_cia_aberta_BPA_con_' + str(ano) +'.csv'

    content = zip.open(arquivo, 'r')
    lines = content.readlines()
    newlines = [line.strip().decode('ISO-8859-1') for line in lines]
    newlines = [line.split(';') for line in newlines]
    df = pd.DataFrame(newlines[1:], columns= newlines[0])

    return df

#Retorna Balanço dos passivos da empresa/ano em dataframe
@cache
def get_bs_liabilities_info(ano)-> pd.DataFrame:

    zip = request_data(ano)
    arquivo = 'dfp_cia_aberta_BPP_con_' + str(ano) +'.csv'

    content = zip.open(arquivo, 'r')
    lines = content.readlines()
    newlines = [line.strip().decode('ISO-8859-1') for line in lines]
    newlines = [line.split(';') for line in newlines]
    df = pd.DataFrame(newlines[1:], columns= newlines[0])

    return df

#Retorna DRE da empresa/ano em dataframe
@cache
def get_is_info(ano)-> pd.DataFrame:
    import pandas as pd

    zip = request_data(ano)
    arquivo = 'dfp_cia_aberta_DRE_con_' + str(ano) +'.csv'

    content = zip.open(arquivo, 'r')
    lines = content.readlines()
    newlines = [line.strip().decode('ISO-8859-1') for line in lines]
    newlines = [line.split(';') for line in newlines]
    df = pd.DataFrame(newlines[1:], columns= newlines[0])
    return df

@cache
def get_company_financials(ano, ticker, type) -> pd.DataFrame:
    import pandas as pd
    df = pd.DataFrame()
    match type:
        case 'BPA':
            df = get_bs_assets_info(ano)
        case 'BPP':
            df = get_bs_liabilities_info(ano)
        case 'DRE':
            df = get_is_info(ano)

    tickers = ticker_dict() #dict {ticker:cnpj}

    
    new_df = df.where(df['CNPJ_CIA'] == tickers[ticker])
    new_df.dropna(inplace = True)
    
    
    def left_str(s, separator):
        before_separator, _, _ = s.partition(separator)
        return before_separator

    new_df['VL_CONTA'] = new_df['VL_CONTA'].apply(lambda x : left_str(x,'.') )
    new_df['VL_CONTA'] = new_df['VL_CONTA'].astype('int64')
    new_df.reset_index(inplace = True)
    return new_df


def clas_setorial_excel() -> pd.DataFrame:
    import zipfile
    import io
    import pandas as pd

    zip = request_clas_setorial()

    zip_ref = zipfile.ZipFile(io.BytesIO(zip.content), 'r')
    arquivo = 'Setorial B3 14-05-2024 (português).xlsx'

    with zip_ref.open(arquivo) as file:
        df = pd.read_excel(io.BytesIO(file.read()), skiprows= 8, header= None)
    headers = ['Setor', 'Subsetor', 'Segmento', 'Ticker', 'Segmento de listagem']
    df.columns = headers

    #"Explode" do segmento
    for i in range(1, len(df)):
        if pd.notna(df.loc[i, 'Ticker']):
            df.loc[i,'Segmento'] = df.loc[i-1,'Segmento']


    #"Explode" do subsetor e setor 
    df['Subsetor'] = df['Subsetor'].ffill()
    df['Setor'] = df['Setor'].ffill()

    df = df.dropna(subset=['Segmento','Ticker'])

    df.reset_index(inplace=True)
    df.set_index('Ticker', inplace = True )
    df.to_excel('data/Clas_Setorial.xlsx', index = True)
    return df


@cache
def clas_setorial() -> pd.DataFrame:
    import os
    import pandas as pd

    arquivos = os.listdir('data')
    if 'Clas_Setorial.xlsx' not in arquivos:
        df = clas_setorial_excel(index = 0)
        return df

    df = pd.read_excel('data/Clas_Setorial.xlsx', index_col= 'Ticker')
    return df



def company_type(ticker):
    ticker = ticker[:4]
    df = clas_setorial()
    setor = df.loc[ticker,'Setor']
    subsetor = df.loc[ticker,'Subsetor']
    segmento = df.loc[ticker,'Segmento']
    _dict = {'Setor': setor, 'Subsetor':subsetor, 'Segmento': segmento}
    return _dict
    
