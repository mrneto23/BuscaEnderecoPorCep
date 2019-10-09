# Busca endereco por CEP.

Script que busca as informações do endereço usando o CEP.

```python
from BuscaEnderecoPorCep import BuscaEndereco

endereco = BuscaEndereco(13015090)
print(endereco)
```

```
{'cep': '13015-090', 'logradouro': 'Rua Dona Libânia', 'complemento': '', 'bairro': 'Centro', 'localidade': 'Campinas', 'uf': 'SP', 'unidade': '', 'ibge': '3509502', 'gia': '2446'}
```
