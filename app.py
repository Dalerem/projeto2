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

class Requisicao:

    def get(self):
        cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
        cotas = cotacoes.json()

        cotacao_dolar = cotas["USDBRL"]["bid"]
        cotacao_euro = cotas["EURBRL"]["bid"]
        cotacao_btc = cotas["BTCBRL"]["bid"]

        return cotacao_dolar, cotacao_euro, cotacao_btc

resp = Requisicao()

print("Cotações do Dolar, Euro e Btc:", resp.get())
