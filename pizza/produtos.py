# -*- coding: iso-8859-1 -*-
# -*- Mode: Python; py-indent-offset: 4 -*-

from sqlobject import *

from pizza.conexao import Conexao
__connection__ = Conexao



class Massa(SQLObject):
    nome = StringCol(length=100, notNull=1)
    sabor = ForeignKey('Sabor', notNull=1)
    preco = DecimalCol(size=5, precision=2, notNull=1)


class Lanche(SQLObject):
    nome = StringCol(length=100, notNull=1)
    sabor = ForeignKey('Sabor', notNull=1)
    preco = DecimalCol(size=5, precision=2, notNull=1)


class Bebida(SQLObject):
    nome = StringCol(length=100, notNull=1)
    tipo = StringCol(length=100, notNull=1)
    preco = DecimalCol(size=5, precision=2, notNull=1)


class Sobremesa(SQLObject):
    nome = StringCol(length=100, notNull=1)
    tipo = StringCol(length=100, notNull=1)
    preco = DecimalCol(size=5, precision=2, notNull=1)


class Outro(SQLObject):
    nome = StringCol(length=100, notNull=1)
    tipo = StringCol(length=100, notNull=1)
    preco = DecimalCol(size=5, precision=2, notNull=1)


class Sabor(SQLObject):
    nome = StringCol(length=100, notNull=1)
    ingredientes = StringCol(notNull=1)
