import requests

"""
    Requisição de API de cotações

    Autohr: Dálerem Teixeira
    E-mail: dalerem2022@gmail.com
    Linkedin: https://www.linkedin.com/in/d%C3%A1lerem-teixeira-949a48236/
"""

__Author__ = "Dálerem Teixeira"
__Email__ = "dalerem2022@gmail.com"
__Linkedin__ = "https://www.linkedin.com/in/d%C3%A1lerem-teixeira-949a48236/"

class Requisicao_api:
    """
        Classe de Requisição de api
    """
    def __init__(self, cot):
        self.cot = cot
    def dolar(self):
        cotacao_dolar = self.cot["USDBRL"]["bid"]
        return cotacao_dolar
    def euro(self):
        cotacao_euro = self.cot["EURBRL"]["bid"]
        return cotacao_euro
    def btc(self):
        cotacao_btc = self.cot["BTCBRL"]["bid"]
        return cotacao_btc

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotas = cotacoes.json()

resp = Requisicao_api(cotas)

print("Cotações do Dolar:", resp.dolar())
print("Cotações do Euro:", resp.euro())
print("Cotações do Btc:", resp.btc())