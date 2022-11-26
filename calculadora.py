"""
Calculadora com as quatro operacao
"""
class Calculadora:
    """inicializa as variaveis"""
    def __init__(self):
        """variaveis de escopo da classe"""
        self.soma = 0
        self.resultado_sub = 0

    def adicao(self,var1, var2):
        """soma as variaveis"""
        self.soma = var1 + var2
        return self.soma

    def subtracao(self, var2, var1) :
        """retorna a subtracao de dois numeros"""
        self.resultado_sub = var2 - var1
        return self.resultado_sub

calc = Calculadora()
calc.adicao(1,4)
calc.subtracao(5,4)

print(calc.soma)
print(calc.resultado_sub)