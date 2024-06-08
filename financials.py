from utils import (get_company_financials,
                   company_type)
import pandas as pd
def financials(start,end,ticker):
    clas_setor = company_type(ticker)
    
    nr_conta = 'CD_CONTA'
    exercicio = 'ORDEM_EXERC'
    valor = 'VL_CONTA'
    start = 2010 if start < 2010 else start
    end = 2023 if end >= 2024 else end
    
    def lucro_liquido(start, end, ticker):
        _list_lucro = {}

        ## empresas ñ financeiras acho que era 3.11 para lucro liquido
        hashmap = { 'Petróleo, Gás e Biocombustíveis': '3.11',
            'Materiais Básicos' : '3.11',
            'Bens Industriais' : '3.11',
            'Consumo não Cíclico' : '3.11',
            'Consumo Cíclico' : '3.11',
            'Saúde' : '3.11',
            'Tecnologia da Informação' : '3.11',
            'Comunicações' : '3.11',
            'Utilidade Pública' : '3.11',
            'Financeiro': '3.09',
            'Outros': '3.11',
        }
        for i in range(start,end+1):
            
            if str(i+1) not in _list_lucro:
                df = get_company_financials(i,ticker,'DRE')
                
                lucro = df.loc[(df[nr_conta] == hashmap[clas_setor['Setor']]) & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_lucro[i] = lucro
                
                lucro = df.loc[(df[nr_conta] == hashmap[clas_setor['Setor']]) & (df[exercicio] == 'PENÚLTIMO'), valor].sum()
                _list_lucro[i-1] = lucro

        return _list_lucro
    
    def ebit(start, end, ticker):
        _list_ebit = {}
        hashmap = { 'Nome do setor' : 'Respectiva conta (para cada ffigure)'


        }

        for i in range(start, end+1):
            if str(i+1) not in _list_ebit:
                df = get_company_financials(i,ticker,'DRE')
                #Valores do ebit para cada ano
                
                ebit = df.loc[(df[nr_conta] == '3.05') & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_ebit[i] = ebit
                
                ebit = df.loc[(df[nr_conta] == '3.05') & (df[exercicio] == 'PENÚLTIMO'),valor].sum()
                _list_ebit[i-1] = ebit

            #lista de depreciação e amortização para cada ano
            #EBITDA = RESULTADO LIQUIDO DO EXERCICIO ('3.09') + IRPJ/CSSL corrente e diferido('3.08') + Resultado financeiro('3.06') + Depreciação e amortização('6.01.01.02')

        return _list_ebit

    def pl(start, end, ticker):
        _list_pl = {}
        hashmap = { 'Nome do setor' : 'Respectiva conta (para cada ffigure)'


        }
        for i in range(start, end +1):
            if str(i+1) not in _list_pl:
                df = get_company_financials(i,ticker,'BPP')
                pl = df.loc[(df[nr_conta] == '2.03') & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_pl[i] = pl

                pl = df.loc[(df[nr_conta] == '2.03') & (df[exercicio] == 'PENÚLTIMO'), valor].sum()
                _list_pl[i-1] = pl
        return _list_pl
    

    def passivo(start, end, ticker):
        _list_passivo = {}
        hashmap = { 'Nome do setor' : 'Respectiva conta (para cada ffigure)'


        }
        for i in range(start, end +1):
            if str(i+1) not in _list_passivo:
                df = get_company_financials(i,ticker, 'BPP')
                ev = df.loc[((df[nr_conta] == '2.01') | (df[nr_conta] == '2.02')) & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_passivo[i] = ev

                ev = df.loc[((df[nr_conta] == '2.01') | (df[nr_conta] == '2.02')) & (df[exercicio] == 'PENÚLTIMO'), valor].sum()
                _list_passivo[i-1] = ev
            
        return _list_passivo
                
    def receita_liquida(start,end,ticker):
        _list_receita_liquida = {}    

        for i in range(start, end+1):
            if str(i+1) not in _list_receita_liquida:
                df = get_company_financials(i,ticker,'DRE')
                #Valores do ebit para cada ano
                
                receita = df.loc[(df[nr_conta] == '3.01') & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_receita_liquida[i] = receita
                
                receita = df.loc[(df[nr_conta] == '3.01') & (df[exercicio] == 'PENÚLTIMO'),valor].sum()
                _list_receita_liquida[i-1] = receita
        return _list_receita_liquida


    def cpv(start,end,ticker):
        _list_cpv = {}

        for i in range(start, end+1):
            if str(i+1) not in _list_cpv:
                df = get_company_financials(i,ticker,'DRE')
                #Valores do ebit para cada ano
                
                cpv = df.loc[(df[nr_conta] == '3.02') & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_cpv[i] = cpv
                
                cpv = df.loc[(df[nr_conta] == '3.02') & (df[exercicio] == 'PENÚLTIMO'),valor].sum()
                _list_cpv[i-1] = cpv
        
        return _list_cpv
            
    def sga(start, end, ticker):
        _list_sga = {}        
        start = 2010 if start < 2010 else start

        for i in range(start, end+1):
            if str(i+1) not in _list_sga:
                df = get_company_financials(i,ticker,'DRE')
                #Valores do ebit para cada ano
                
                sga = df.loc[(df[nr_conta] == '3.04') & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_sga[i] = sga
                
                sga = df.loc[(df[nr_conta] == '3.04') & (df[exercicio] == 'PENÚLTIMO'),valor].sum()
                _list_sga[i-1] = sga
        
        return _list_sga

    print(lucro_liquido(start,end,ticker))

    # _list_lucro = lucro(start, end, ticker)
    # _list_ebit = ebit(start,end,ticker)
    # _list_pl = pl(start,end,ticker)
    # _list_ev = passivo(start,end,ticker)
    
    # print('ev', ticker, _list_ev)



financials(2019 ,2024,'HAPV3')



x= {'3.04.07.01': 'Amortização de intangivel (Despesa)',
 '3.04.07.03': 'Depreciação (Despesa)',
 '3.02.06': 'Depreciação (Custos)',
'3.02.07': 'Amortização (Custos)',
'3.04.02.07': 'Depreciação (Despesa)',
'3.04.02.08': 'Amortização (Despesa)',
}
