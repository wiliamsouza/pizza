# -*- coding: iso-8859-1 -*-
# -*- Mode: Python; py-indent-offset: 4 -*-

from sqlobject import connectionForURI

servidor = 'localhost'
banco = 'mysql'
basedados = 'pizza'
usuario = 'root'
senha = '123456'

# Uso: "banco://usuario:senha@servidor/basedados"
Conexao = connectionForURI('%s://%s:%s@%s/%s' % \
                       (banco, usuario, senha, servidor, basedados))
