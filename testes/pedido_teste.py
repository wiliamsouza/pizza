# -*- coding: iso-8859-1 -*-
# -*- Mode: Python; py-indent-offset: 4 -*-

import unittest

from pizza.pedido import Pedido, Conteudo, Entregador, Tamanho
from pizza.cliente import Pessoa
from pizza.produtos import Massa, Sabor



class TestePedido(unittest.TestCase):

    def setUp(self):
        self.pessoa_ = Pessoa(nome='Wiliam Alves de Souza',
                             residencial='00 0000 0000',
                             celular='00 0000 0000',
                             recado='00 0000 0000',
                             nascimento='06/06/1981',
                             sexo='M',
                             email='wiliamsouza83@gmail.com',
                             observacao='Teste observação')

        self.sabor = Sabor(nome='Mussarela',
                           ingredientes='Mussarela, Tomate e Molho')

        self.massa = Massa(nome='Pizza',
                           sabor=self.sabor,
                           preco=99.99)

        self.tamanhoEntrada = Tamanho(tamanho='Pequeno')
        self.tamanhoSaida = Tamanho.get(self.tamanhoEntrada.id)

        self.entregadorEntrada = Entregador(nome='Wiliam Alves de Souza',
                                            residencial='00 0000 0000',
                                            celular='00 0000 0000')
        self.entregadorSaida = Entregador.get(self.entregadorEntrada.id)
        
        self.pedidoEntrada = Pedido(pessoa=self.pessoa_,
                                    data='2005-09-23',
                                    estado='Aberto',
                                    entregador=self.entregadorSaida)
	self.pedidoSaida = Pedido.get(self.pedidoEntrada.id)

        self.conteudoEntrada = Conteudo(pedido=self.pedidoSaida,
                                        produtos_id=['1', '2', '3'],
                                        tamanho=self.tamanhoSaida,
                                        quantidade=99,
                                        observacao='Teste observação')
        self.conteudoSaida = Conteudo.get(self.conteudoEntrada.id)

    def testTamanho(self):
        self.assertEqual(self.tamanhoEntrada.tamanho,
                         self.tamanhoSaida.tamanho)

    def testEntregador(self):
        self.assertEqual(self.entregadorEntrada.nome,
                         self.entregadorSaida.nome)
        self.assertEqual(self.entregadorEntrada.residencial,
                         self.entregadorSaida.residencial)
        self.assertEqual(self.entregadorEntrada.celular,
                         self.entregadorSaida.celular)

    def testPedido(self):
        self.assertEqual(self.pedidoEntrada.pessoa, self.pedidoSaida.pessoa)
        self.assertEqual(self.pedidoEntrada.data, self.pedidoSaida.data)
        self.assertEqual(self.pedidoEntrada.estado, self.pedidoSaida.estado)
        self.assertEqual(self.pedidoEntrada.entregador,
                         self.pedidoSaida.entregador)

    def testConteudo(self):
        self.assertEqual(self.conteudoEntrada.pedido,
                         self.conteudoSaida.pedido)
        self.assertEqual(self.conteudoEntrada.produtos_id,
                         self.conteudoSaida.produtos_id)
        self.assertEqual(self.conteudoEntrada.tamanho,
                         self.conteudoSaida.tamanho)
        self.assertEqual(self.conteudoEntrada.quantidade,
                         self.conteudoSaida.quantidade)
        self.assertEqual(self.conteudoEntrada.observacao,
                         self.conteudoSaida.observacao)

if __name__ == "__main__":
	unittest.main()
