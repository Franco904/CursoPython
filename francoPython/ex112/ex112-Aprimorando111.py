from ex112.utilidades import moeda
from ex112.utilidades import dados

dinheiro = dados.leiadinheiro('Informe um preço para operação: ')
moeda.resumo(dinheiro, 80, 35)