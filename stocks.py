from utils import (company_type)
from financials import financials

class stock:
    def __init__(self,start,end, ticker):
        
        self.name = ticker
        self.periods = list(range(start,end +1))
        self.cotacao = 1 ## N.Y.I

        class_setorial = company_type(ticker)
        contas_resultado = financials(start,end,ticker)

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

    def add(self, start, end):
        for i in range(start,end,1):
            if i not in (self.periods):
                contas_resultado = financials(i,i,self.name)
                self.lucro_liquido[i] = contas_resultado['Lucro Liquido'][i]
                self.ebit[i] = contas_resultado['EBIT'][i]
                self.pl[i] = contas_resultado['Patrimonio Liquido'][i]
                self.pc[i] = contas_resultado['Passivo Circulante'][i]
                # self.pnc = self.pnc + [{k:v} for k,v in enumerate(contas_resultado['Passivo n Circulante'])]
                # self.rl += [{k,v} for k,v in enumerate(contas_resultado['Receita Liquida'])]
                # self.cpv += [{k,v} for k, v in  enumerate(contas_resultado['CPV'])]
                # self.sga += [{k,v} for k, v in  enumerate(contas_resultado['SG_A'])]
                # self.da += [{k,v} for k, v in  enumerate(contas_resultado['D_A'])]
                # self.ac += [{k,v} for k, v in  enumerate(contas_resultado['Ativo Circulante'])]
                # self.anc += [{k,v} for k, v in  enumerate(contas_resultado['Ativo n Circulante'])]


    def preco_lucro(self, start, end):
        if not (start in self.periods and end in self.periods):
            self.add(start,end)
        lucro = []
        for i in range(start,end+1):
            lucro += self.lucro_liquido[i]
        lucro_medio = lucro.mean()

        self.preco_lucro =  self.cotacao / lucro_medio
           
        
    def sales_to_capital_ratio(self,start,end):
        if not (start - 1  in self.periods):
            self.add(self,start-1,start)
        _list_
        for i in range(start,end):

            
            
        ind = self.rl / ()
        ## Net Rev. / (Ativo do periodo anterior - Caixa e Equivalentes de Caixa do periodo anterior) 

        
        
        
        ...