# -*- coding: iso-8859-1 -*-
# -*- Mode: Python; py-indent-offset: 4 -*-

import unittest

from pizza.produtos import Massa, Lanche, Bebida, Sobremesa, Outro, Sabor



class TesteProdutos(unittest.TestCase):

    def setUp(self):
        self.saborEntrada = Sabor(nome='Mussarela',
                                  ingredientes='Mussarela, Tomate e Molho')
        self.saborSaida = Sabor.get(self.saborEntrada.id)

        self.massaEntrada = Massa(nome='Pizza',
                                  sabor=self.saborSaida,
                                  preco=99.99)
        self.massaSaida = Massa.get(self.massaEntrada.id)

        self.lancheEntrada = Lanche(nome='Cheese',
                                    sabor=self.saborSaida,
                                    preco=99.99)
        self.lancheSaida = Lanche.get(self.lancheEntrada.id)

        self.bebidaEntrada = Bebida(nome='Refrigerante',
                                    tipo='Coca',
                                    preco=99.99)
        self.bebidaSaida = Bebida.get(self.bebidaEntrada.id)

        self.sobremesaEntrada = Sobremesa(nome='Bombom',
                                          tipo='Morango',
                                          preco=99.99)
        self.sobremesaSaida = Sobremesa.get(self.sobremesaEntrada.id)

        self.outroEntrada = Outro(nome='Bala',
                                  tipo='iogurte',
                                  preco=99.99)
        self.outroSaida = Outro.get(self.outroEntrada.id)

    def testSabor(self):
        self.assertEqual(self.saborEntrada.nome, self.saborSaida.nome)
        self.assertEqual(self.saborEntrada.ingredientes,
                         self.saborSaida.ingredientes)

    def testMassa(self):
        self.assertEqual(self.massaEntrada.nome, self.massaSaida.nome)
        self.assertEqual(self.massaEntrada.sabor, self.massaSaida.sabor)
        self.assertEqual(self.massaEntrada.preco, self.massaSaida.preco)

    def testLanche(self):
        self.assertEqual(self.lancheEntrada.nome, self.lancheSaida.nome)
        self.assertEqual(self.lancheEntrada.sabor, self.lancheSaida.sabor)
        self.assertEqual(self.lancheEntrada.preco, self.lancheSaida.preco)

    def testBebida(self):
        self.assertEqual(self.bebidaEntrada.nome, self.bebidaSaida.nome)
        self.assertEqual(self.bebidaEntrada.tipo, self.bebidaSaida.tipo)
        self.assertEqual(self.bebidaEntrada.preco, self.bebidaSaida.preco)

    def testSobremesa(self):
        self.assertEqual(self.sobremesaEntrada.nome,
                         self.sobremesaSaida.nome)
        self.assertEqual(self.sobremesaEntrada.tipo,
                         self.sobremesaSaida.tipo)
        self.assertEqual(self.sobremesaEntrada.preco,
                         self.sobremesaSaida.preco)

    def testOutro(self):
        self.assertEqual(self.outroEntrada.nome, self.outroSaida.nome)
        self.assertEqual(self.outroEntrada.tipo, self.outroSaida.tipo)
        self.assertEqual(self.outroEntrada.preco, self.outroSaida.preco)

if __name__ == "__main__":
	unittest.main()
