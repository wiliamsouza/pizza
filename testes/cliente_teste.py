# -*- coding: iso-8859-1 -*-
# -*- Mode: Python; py-indent-offset: 4 -*-

import unittest

from pizza.cliente import Pessoa, Endereco



class TesteCliente(unittest.TestCase):

    def setUp(self):
        self.pessoaEntrada = Pessoa(nome='Wiliam Alves de Souza',
                                    residencial='00 0000 0000',
                                    celular='00 0000 000',
                                    recado='00 0000 0000',
                                    nascimento='06/06/1981',
                                    sexo='M',
                                    email='wiliamsouza83@gmail.com',
                                    observacao='Teste observação')
        self.pessoaSaida = Pessoa.get(self.pessoaEntrada.id)

        self.enderecoEntrada = Endereco(pessoa=self.pessoaSaida,
                                        cidade='Curitiba',
                                        cep='000 000 000',
                                        rua='Das Tartarugas',
                                        numero='23',
                                        complemento='Casa 01',
                                        referencia='AlphaWili',
                                        bairro='Jardim Paraná',
                                        preco_entrega=999.99)
        self.enderecoSaida = Endereco.get(self.enderecoEntrada.id)

    def testPessoa(self):
        self.assertEqual(self.pessoaEntrada.nome,
                         self.pessoaSaida.nome)
        self.assertEqual(self.pessoaEntrada.residencial,
                         self.pessoaSaida.residencial)
        self.assertEqual(self.pessoaEntrada.celular,
                         self.pessoaSaida.celular)
        self.assertEqual(self.pessoaEntrada.recado,
                         self.pessoaSaida.recado)
        self.assertEqual(self.pessoaEntrada.nascimento,
                         self.pessoaSaida.nascimento)
        self.assertEqual(self.pessoaEntrada.sexo,
                         self.pessoaSaida.sexo)
        self.assertEqual(self.pessoaEntrada.email,
                         self.pessoaSaida.email)
        self.assertEqual(self.pessoaEntrada.observacao,
                         self.pessoaSaida.observacao)

    def testEndereco(self):
        self.assertEqual(self.enderecoEntrada.pessoa,
                         self.enderecoSaida.pessoa)
        self.assertEqual(self.enderecoEntrada.cidade,
                         self.enderecoSaida.cidade)
        self.assertEqual(self.enderecoEntrada.cep,
                         self.enderecoSaida.cep)
        self.assertEqual(self.enderecoEntrada.rua,
                         self.enderecoSaida.rua)
        self.assertEqual(self.enderecoEntrada.numero,
                         self.enderecoSaida.numero)
        self.assertEqual(self.enderecoEntrada.complemento,
                         self.enderecoSaida.complemento)
        self.assertEqual(self.enderecoEntrada.referencia,
                         self.enderecoSaida.referencia)
        self.assertEqual(self.enderecoEntrada.bairro,
                         self.enderecoSaida.bairro)
        self.assertEqual(self.enderecoEntrada.preco_entrega,
                         self.enderecoSaida.preco_entrega)

if __name__ == "__main__":
	unittest.main()
