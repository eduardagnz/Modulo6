

class ProdutosService():
    def __init__(self, tipo, valor, juros, retorno):
        self.tipo = tipo
        self.valor = valor
        self.juros = juros
        self.retorno = retorno
        # conecta ao banco de dados
        
    def valor_retorno(self):
        #verifica 
        valor_retorno = self.valor * self.juros
        return valor_retorno
    
    def cadastro(self):
        #inputa no banco
        
        token = "registred"
        return token