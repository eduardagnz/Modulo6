from model import ProdutosService


def valor_retorno(valor, juros):
    
    try:
        service = valor_retorno(valor = valor, juros = juros)
        
        token = service.cadastro()
        
        return token
    except IndexError:
        return 