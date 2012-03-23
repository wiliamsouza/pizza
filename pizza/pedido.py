# -*- coding: iso-8859-1 -*-
# -*- Mode: Python; py-indent-offset: 4 -*-

from sqlobject import *

from pizza.conexao import Conexao
__connection__ = Conexao



class Pedido(SQLObject):

    pessoa = ForeignKey('Pessoa', notNull=1)
    data = StringCol(length=10, notNull=1)
    estado = StringCol(length=10, notNull=1)
    entregador = ForeignKey('Entregador', notNull=1)


class Conteudo(SQLObject):

    pedido = ForeignKey('Pedido', notNull=1)
    produtos_id = StringCol(notNull=1)
    tamanho = ForeignKey('Tamanho', notNull=1)
    quantidade = IntCol(notNull=1)
    observacao = StringCol(notNull=1)

    def _set_produtos_id(self, lista_id):

        """ Recebe uma lista de inteiros(int) ou caracteres(string)
        junta os valores separando-os com um espaço e grava no banco
        como texto(text).
        """
        if not isinstance(lista_id, list):
            raise ValueError, "Forneca um lista com os ID's dos produtos"
        self._SO_set_produtos_id(' '.join(map(str, lista_id)))

    def _get_produtos_id(self):

        """ Retorna uma lista de inteiros(int) com ID's dos produtos"""
        return self._SO_get_produtos_id().split(' ')


class Entregador(SQLObject):

    nome = StringCol(length=100, notNull=1)
    residencial = StringCol(length=12, notNull=1 )
    celular = StringCol(length=12, notNull=1)


class Tamanho(SQLObject):

    tamanho = StringCol(length=100, notNull=1)
