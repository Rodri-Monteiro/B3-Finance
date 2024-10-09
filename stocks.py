from utils import (company_type)
from financials import financials

class stock:
    def __init__(self,start,end, ticker):
        class_setorial = company_type(ticker)
        contas_resultado = financials(start,end,ticker)
        
        self.name = ticker

        self.setor = class_setorial['Setor']
        self.subsetor = class_setorial['Subsetor']
        self.segmento = class_setorial['Segmento']

        self.lucro_liquido = contas_resultado['Lucro Liquido']
        self.ebit = contas_resultado['EBIT']
        self.pl = contas_resultado['Patrimonio Liquido']
        self.pc = contas_resultado['Passivo Circulante']
        self.pnc = contas_resultado['Passivo n Circulante']
        self.rl = contas_resultado['Receita Liquida']
        self.cpv = contas_resultado['CPV']
        self.sga = contas_resultado['SG_A']
        self.da = contas_resultado['D_A']
        self.ac = contas_resultado['Ativo Circulante']
        self.anc = contas_resultado['Ativo n Circulante']

        


