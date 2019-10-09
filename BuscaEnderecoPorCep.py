import urllib.request
import json


class BuscaEndereco(object):
    """docstring for BuscaEndereco"""

    def __init__(self, cep):
        super(BuscaEndereco, self).__init__()
        self.cep = cep
        self.url = "http://viacep.com.br/ws/%s/json"
        self.endereco = json.load(urllib.request.urlopen(self.url % self.cep))
        self.cep = self.endereco['cep']
        self.logradouro = self.endereco['logradouro']
        self.complemento = self.endereco['complemento']
        self.bairro = self.endereco['bairro']
        self.cidade = self.endereco['localidade']
        self.uf = self.endereco['uf']
        self.unidade = self.endereco['unidade']
        self.ibge = self.endereco['ibge']
        self.gia = self.endereco['gia']

    def __str__(self):
        return "%s" % (self.endereco)

    def getEndereco(self):
        return self.endereco
