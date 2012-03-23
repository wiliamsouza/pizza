# -*- coding: iso-8859-1 -*-
# -*- Mode: Python; py-indent-offset: 4 -*-

from sqlobject import *

from pizza.conexao import Conexao
__connection__ = Conexao



class Pessoa(SQLObject):

    """ Classe reponsável pela leitura e gravação dos
    dados da pessoa.
    
    Uso para gravação:
    pessoa = Pessoa(nome='Wiliam Alves de Souza',
                    residencial='00 0000 0000',
                    celular='00 0000 000',
                    recado='00 0000 0000',
                    nascimento='06/06/1981',
                    sexo='M',
                    email='wiliamsouza83@gmail.com',
                    observacao='Teste observação')

    Uso para leitura:
    for pessoa in Pessoa.select():
        print pessoa.nome
        print pessoa.residencial
        print pessoa.celular
        print pessoa.recado
        print pessoa.nascimento
        print pessoa.sexo
        print pessoa.email
        print pessoa.observacao
    """
    nome = StringCol(length=100, notNull=1)
    residencial = StringCol(length=12, notNull=1 )
    celular = StringCol(length=12, notNull=1)
    recado = StringCol(length=12, notNull=1)
    nascimento = StringCol(length=10, notNull=1)
    sexo = StringCol(length=1, notNull=1)
    email = StringCol(length=100, notNull=1)
    observacao = StringCol(notNull=1)


class Endereco(SQLObject):

    """Classe reponsável pela leitura e gravação do
    endereço da pessoa.
    
    Uso para gravação:
    endereco = Endereco(pessoa=self.pessoa,
                        cidade='Curitiba',
                        cep='000 000 000',
                        rua='Das Tartarugas',
                        numero='23',
                        complemento='Casa 01',
                        referencia='AlphaWili',
                        bairro='Jardim Paraná',
                        preco_entrega=999.99)

    Uso para leitura:
    for endereco in Endereco.select():
        print endereco.pessoa
        print endereco.cidade
        print endereco.cep
        print endereco.rua
        print endereco.numero
        print endereco.complemento
        print endereco.referencia
        print endereco.bairro
        print endereco.preco_entrega
    """
    pessoa = ForeignKey('Pessoa', notNull=1)
    cidade = StringCol(length=30, notNull=1)
    cep = StringCol(length=10, notNull=1)
    rua = StringCol(length=100, notNull=1)
    numero = StringCol(length=10, notNull=1)
    complemento = StringCol(length=100, notNull=1)
    referencia = StringCol(length=100, notNull=1)
    bairro = StringCol(length=50, notNull=1)
    preco_entrega = DecimalCol(size=5, precision=2, notNull=1)
