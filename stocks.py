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
        self.caixa = contas_resultado['Caixa']
        self.aplicacoes_financeiras = contas_resultado['Aplicacoes financeiras']
        
        ##indicadores
        self.preco_lucro = None
        self.sales_to_capital_ratio = None
        self.working_capital = None

    def add(self, start, end):
        start = 2011 if start < 2011 else start

        for i in range(start,end+1,1):
            if i not in (self.periods):
                contas_resultado = financials(i,i,self.name)
                self.lucro_liquido[i] = contas_resultado['Lucro Liquido'][i]
                self.ebit[i] = contas_resultado['EBIT'][i]
                self.pl[i] = contas_resultado['Patrimonio Liquido'][i]
                self.pc[i] = contas_resultado['Passivo Circulante'][i]
                self.pnc[i] = contas_resultado['Passivo n Circulante'][i]
                self.rl[i] = contas_resultado['Receita Liquida'][i]
                self.cpv[i] = contas_resultado['CPV'][i]
                self.sga[i] = contas_resultado['SG_A'][i]
                self.da[i] = contas_resultado['D_A'][i]
                self.ac[i] = contas_resultado['Ativo Circulante'][i]
                self.anc[i] = contas_resultado['Ativo n Circulante'][i]
                self.caixa[i] = contas_resultado['Caixa'][i]
                self.aplicacoes_financeiras[i] = contas_resultado['Aplicacoes financeiras'][i]



    def preco_lucro_(self, start, end):
        if not (start in self.periods and end in self.periods):
            self.add(start,end)
        lucro = []
        for i in range(start,end+1):
            lucro += self.lucro_liquido[i]
        lucro_medio = lucro.mean()

        self.preco_lucro =  self.cotacao / lucro_medio

    def sales_to_capital_ratio_(self,start,end):
        if self.sales_to_capital_ratio is None:
            if not (start - 1  in self.periods):
                self.add(start,start)
            _list = {}    
            for i in range(start,end+1):
                _list[i] = self.rl[i] / (self.ac[i-1] + self.anc[i-1] - self.caixa[i-1] - self.aplicacoes_financeiras[i-1])

            self.sales_to_capital_ratio = _list
        return self.sales_to_capital_ratio
    
        ## Formula: Net Revenue Atual / (Ativo do periodo anterior - Caixa e Equivalentes de Caixa do periodo anterior)

    
    def working_capital_(self,start,end):
        if self.working_capital == None:
            ...
        return self.working_capital