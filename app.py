import requests

"""
    Requisição de API de cotações

    Autohr: Dálerem Teixeira
    E-mail: dalerem2022@gmail.com
    Rede_social: https://www.linkedin.com/in/d%C3%A1lerem-teixeira-949a48236/
"""

__author__ = "Dálerem Teixeira"
__Email__ = "dalerem2022@gmail.com"
__redesocial__ = "https://www.linkedin.com/in/d%C3%A1lerem-teixeira-949a48236/"

class Requisicao_api:
    """
        Classe de Requisição de api
    """
    def __init__(self, cot):
        """
            Construtor de cotas

        :param cot: valor para cotas
        """
        self.cot = cot
    def dolar(self):
        """
            Função de cota do dolar

        :return: valor da cota
        """
        cotacao_dolar = self.cot["USDBRL"]["bid"]
        return cotacao_dolar
    def euro(self):
        """
            Função de cota do euro

        :return: valor da cota
        """
        cotacao_euro = self.cot["EURBRL"]["bid"]
        return cotacao_euro
    def btc(self):
        """
            Função do btc

        :return: valor da cota
        """
        cotacao_btc = self.cot["BTCBRL"]["bid"]
        return cotacao_btc

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotas = cotacoes.json()

resp = Requisicao_api(cotas)

print("Cotações do Dolar:", resp.dolar())
print("Cotações do Euro:", resp.euro())
print("Cotações do Btc:", resp.btc())