from utils import (get_company_financials,
                   company_type)
import pandas as pd

def financials(start,end,ticker):
    clas_setor = company_type(ticker)

    
    nome_conta = 'DS_CONTA'
    nr_conta = 'CD_CONTA'
    exercicio = 'ORDEM_EXERC'
    valor = 'VL_CONTA'
    segmento= 'Segmento'

    start = 2010 if start < 2010 else start
    end = 2023 if end >= 2024 else end
    
    def lucro_liquido(start, end, ticker):
        _list_lucro = {}

        hashmap = {'Petróleo, Gás e Biocombustíveis': '3.11',
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
                _list_lucro[i] = int(lucro)
                
                lucro = df.loc[(df[nr_conta] == hashmap[clas_setor['Setor']]) & (df[exercicio] == 'PENÚLTIMO'), valor].sum()
                _list_lucro[i-1] = int(lucro)

        return _list_lucro
    
    def ebit(start, end, ticker):
        _list_ebit = {}

        for i in range(start, end+1):
            if str(i+1) not in _list_ebit:
                df = get_company_financials(i,ticker,'DRE')
                #Valores do ebit para cada ano
                
                ebit = df.loc[(df[nr_conta] == '3.05') & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_ebit[i] = int(ebit)
                
                ebit = df.loc[(df[nr_conta] == '3.05') & (df[exercicio] == 'PENÚLTIMO'),valor].sum()
                _list_ebit[i-1] = int(ebit)

            #lista de depreciação e amortização para cada ano
            #EBITDA = RESULTADO LIQUIDO DO EXERCICIO ('3.09') + IRPJ/CSSL corrente e diferido('3.08') + Resultado financeiro('3.06') + Depreciação e amortização('6.01.01.02')

        return _list_ebit

    def pl(start, end, ticker):
        _list_pl = {}

        for i in range(start, end +1):
            if str(i+1) not in _list_pl:
                df = get_company_financials(i,ticker,'BPP')
                pl = df.loc[(df[nome_conta] == 'Patrimônio Líquido Consolidado') & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_pl[i] = int(pl)

                pl = df.loc[(df[nome_conta] == 'Patrimônio Líquido Consolidado') & (df[exercicio] == 'PENÚLTIMO'), valor].sum()
                _list_pl[i-1] = int(pl)
        return _list_pl

    def passivo_c(start, end, ticker):
        _list_passivo = {}
        hashmap = { 'Nome do setor' : 'Respectiva conta (para cada ffigure)'}

        for i in range(start, end +1):
            if str(i+1) not in _list_passivo:
                df = get_company_financials(i,ticker, 'BPP')
                ev = df.loc[((df[nr_conta] == '2.01')) & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_passivo[i] = int(ev)

                ev = df.loc[((df[nr_conta] == '2.01')) & (df[exercicio] == 'PENÚLTIMO'), valor].sum()
                _list_passivo[i-1] = int(ev)
            
        return _list_passivo

    def passivo_nc(start, end, ticker):
        _list_passivo_nc = {}
        hashmap = { 'Nome do setor' : 'Respectiva conta (para cada ffigure)'


        }
        for i in range(start, end +1):
            if str(i+1) not in _list_passivo_nc:
                
                df = get_company_financials(i,ticker, 'BPP')
                ev = df.loc[((df[nr_conta] == '2.02')) & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_passivo_nc[i] = int(ev)

                ev = df.loc[((df[nr_conta] == '2.02')) & (df[exercicio] == 'PENÚLTIMO'), valor].sum()
                _list_passivo_nc[i-1] = int(ev)
            
        return _list_passivo_nc

    def ativo_c(start, end, ticker):
        _list_ativo = {}

        for i in range(start, end +1):
            if str(i+1) not in _list_ativo:
                df = get_company_financials(i,ticker, 'BPA')
                ac = df.loc[((df[nr_conta] == '1.01')) & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_ativo[i] = int(ac)

                ac = df.loc[((df[nr_conta] == '1.01')) & (df[exercicio] == 'PENÚLTIMO'), valor].sum()
                _list_ativo[i-1] = int(ac)
            
        return _list_ativo

    def ativo_nc(start, end, ticker):
        _list_ativo = {}

        for i in range(start, end +1):
            if str(i+1) not in _list_ativo:
                df = get_company_financials(i,ticker, 'BPA')
                anc = df.loc[((df[nr_conta] == '1.02')) & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_ativo[i] = int(anc)

                anc = df.loc[((df[nr_conta] == '1.02')) & (df[exercicio] == 'PENÚLTIMO'), valor].sum()
                _list_ativo[i-1] = int(anc)
            
        return _list_ativo

    def receita_liquida(start,end,ticker):
        _list_receita_liquida = {}    

        for i in range(start, end+1):
            if str(i+1) not in _list_receita_liquida:
                df = get_company_financials(i,ticker,'DRE')
                #Valores do ebit para cada ano
                
                receita = df.loc[(df[nr_conta] == '3.01') & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_receita_liquida[i] = int(receita)
                
                receita = df.loc[(df[nr_conta] == '3.01') & (df[exercicio] == 'PENÚLTIMO'),valor].sum()
                _list_receita_liquida[i-1] = int(receita)
        return _list_receita_liquida

    def cpv(start,end,ticker):
        _list_cpv = {}

        for i in range(start, end+1):
            if str(i+1) not in _list_cpv:
                df = get_company_financials(i,ticker,'DRE')
                #Valores do ebit para cada ano
                
                cpv = df.loc[(df[nr_conta] == '3.02') & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_cpv[i] = int(cpv)
                
                cpv = df.loc[(df[nr_conta] == '3.02') & (df[exercicio] == 'PENÚLTIMO'),valor].sum()
                _list_cpv[i-1] = int(cpv)

        return _list_cpv

    def sga(start, end, ticker):
        _list_sga = {}        
        start = 2010 if start < 2010 else start
        
        for i in range(start, end+1):
            if str(i+1) not in _list_sga:
                df = get_company_financials(i,ticker,'DRE')
                #Valores do ebit para cada ano
                
                sga = df.loc[(df[nr_conta] == '3.04' ) & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_sga[i] = int(sga)
                
                sga = df.loc[(df[nr_conta] == '3.04') & (df[exercicio] == 'PENÚLTIMO'),valor].sum()
                _list_sga[i-1] = int(sga)
        
        return _list_sga
    
    def d_a(start, end, ticker):
        _list_d_a = {}
        
        for i in range(start,end+1):
            if str(i+1) not in _list_d_a:
                
                #dataframe do DFC do ano e empresa especificados
                df = get_company_financials(i,ticker,'DFC')
                
                d_a = df.loc[((df[nome_conta].str.contains('amortiza', case=False, na=False)) | (df[nome_conta].str.contains('deprecia', case=False, na=False))) & (df[exercicio] == 'ÚLTIMO') & (df[nr_conta].str.contains('6.01.01.', case = False, na = False)), valor].sum()
                _list_d_a[i] = int(d_a)

                d_a = df.loc[((df[nome_conta].str.contains('amortiza', case=False, na=False)) | (df[nome_conta].str.contains('deprecia', case=False, na=False))) & (df[exercicio] == 'PENÚLTIMO') & (df[nr_conta].str.contains('6.01.01.', case = False, na = False)) , valor].sum()
                _list_d_a[i-1] = int(d_a)

        return _list_d_a
    

    def caixa(start, end, ticker):
        _list_caixa = {}        
        start = 2010 if start < 2010 else start
        
        for i in range(start, end+1):
            if str(i+1) not in _list_caixa:
                df = get_company_financials(i,ticker,'BPA')
                
                caixa = df.loc[(df[nr_conta] == '1.01.01' ) & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_caixa[i] = int(caixa)
                
                caixa = df.loc[(df[nr_conta] == '1.01.01') & (df[exercicio] == 'PENÚLTIMO'),valor].sum()
                _list_caixa[i-1] = int(caixa)
        
        return _list_caixa    

    def apl_financeiras_cp(start, end, ticker):
        _list_aplicacoes = {}        
        start = 2010 if start < 2010 else start
        
        for i in range(start, end+1):
            if str(i+1) not in _list_aplicacoes:
                df = get_company_financials(i,ticker,'BPA')
                
                aplicacoes = df.loc[(df[nr_conta] == '1.01.02' ) & (df[exercicio] == 'ÚLTIMO'), valor].sum()
                _list_aplicacoes[i] = int(aplicacoes)
                
                aplicacoes = df.loc[(df[nr_conta] == '1.01.02') & (df[exercicio] == 'PENÚLTIMO'),valor].sum()
                _list_aplicacoes[i-1] = int(aplicacoes)
        
        return _list_aplicacoes    

    ##caixa e eq. (1.01.01) e apl. financeiras (1.01.02)


    _list_financials = {'Lucro Liquido': lucro_liquido(start,end,ticker),
                        'EBIT': ebit(start,end,ticker),
                        'Patrimonio Liquido': pl(start,end,ticker),
                        'Passivo Circulante': passivo_c(start,end,ticker),
                        'Passivo n Circulante': passivo_nc(start,end,ticker),
                        'Receita Liquida': receita_liquida(start,end,ticker),
                        'CPV' : cpv(start,end,ticker),
                        'SG_A' : sga(start,end,ticker),
                        'D_A' : d_a(start,end,ticker),
                        'Ativo Circulante': ativo_c(start,end,ticker),
                        'Ativo n Circulante': ativo_nc(start,end,ticker),
                        'Caixa' : caixa(start, end, ticker),
                        'Aplicacoes financeiras' : apl_financeiras_cp(start,end,ticker)
                        }
    
    return _list_financials

