import urllib.request
import json


class BuscaEndereco(object):
    """docstring for BuscaEndereco"""


    def __init__(self, cep):
        super(BuscaEndereco, self).__init__()
        self.cep = cep
        self.url = "http://viacep.com.br/ws/%s/json"
        self.endereco = json.load(urllib.request.urlopen(self.url % self.cep))


    def __str__(self):
        return "%s" % (self.endereco)


    def getEndereco(self):
        return self.endereco

