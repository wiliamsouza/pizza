# -*- coding: iso-8859-1 -*-
# -*- Mode: Python; py-indent-offset: 4 -*-

try:
    import pygtk
    pygtk.require('2.0')
    import gtk, gtk.glade
except (ImportError, AssertionError):
    raise SystemExit, 'Primeiro instale o PyGTK (http://www.pygtk.org/)'

from pizza.interface.clientegui import ClienteGTK
##from pizza.interface.tamanhogui import TamanhoGTK
from pizza.interface.saborgui import SaborGTK



class PizzaGTK:

    def __init__(self):
        # Carrega arquivo ".glade".
        self.xml = gtk.glade.XML('glade/pizza.glade')

        # Conecta os sinais automaticamente.
        self.xml.signal_autoconnect(self)

        # Pega a janela principal.
        self.pizza = self.xml.get_widget('pizza')

        # Pega o diálogo sobre.
        self.sobre = self.xml.get_widget('sobre')

        # Instancia interface clienteGTK
        self.cliente = ClienteGTK()

        # Instancia interface TamanhoGTK
#        self.tamanho = TamanhoGTK()

        # Instancia interface SaborGTK
        self.sabor = SaborGTK()

    # Manipuladores dos menus -----------------------------------------
    
    def on_conectar_activate(self,button):
        # Mostra diálogo conectar
        print 'Menu arquivo->conectar pressionado'

    def on_sair_activate(self, button):
        # Fecha janela e encerra o programa
        print 'Menu arquivo->sair presionado'
        gtk.main_quit()

    def on_massa_activate(self, button):
        # Mostra diálogo nova massa
        print 'Menu novo->produto->massa pressionado'

    def on_lanche_activate(self, button):
        # Mostra diálogo novo lanche
        print 'Menu novo->produto->lanche pressionado'

    def on_bebida_activate(self, button):
        # Mostra diálogo nova bebida 
        print 'Menu novo->produto->bebida pressionado'

    def on_sobremesa_activate(self, button):
        # Mostra diálogo nova sobremesa
        print 'Menu novo->produto->sobremesa pressionado'

    def on_outro_activate(self, button):
        # Mostra diálogo novo outro
        print 'Menu novo->produto->outro pressionado'

    def on_sabor_activate(self, button):
        # Mostra diálogo novo sabor
        print 'Menu novo->sabor pressionado'
        self.sabor.mostrar_janela()

    def on_tamanho_activate(self, button):
        # Mostra diálogo novo tamanho
        print 'Menu novo->tamanho pressionado.'

    def on_cliente_activate(self, button):
        # Mostra diálogo novo cliente
        print 'Menu novo->cliente pressionado'
        self.cliente.mostrar_janela()

    def on_entregador_activate(self, button):
        # Mostra diálogo novo entregador
        print 'Menu novo->entregador pressionado'

    def on_sobre_activate(self, button):
        # Mostra o diálogo sobre.
        print 'Menu ajuda->sobre pressionado.'
        self.sobre.show()


    # Manipuladores dos botões -------------------------------------------
    
    def on_listar_clicked(self, button):
        # Mostra diálogo listar clientes
        print 'Botão listar clientes pressionado.'

    def on_novo_clicked(self, button):
        # Mostra diálogo novo cliente.
        print 'Botão novo cliente pressionado.'
        self.cliente.mostrar_janela()

    def on_remover_clicked(self, button):
        # Remove conteúdo do pedido.
        print 'Botão remover conteudo pressionado.'

    def on_adicionar_clicked(self, button):
        # Adiciona conteúdo ao pedido.
        print 'Botão adicionar conteudo pressionado'

    def on_executar_clicked(self, button):
        # Executa pedido.
        print 'Botão executar pedido pressionado.'

    # Manipuladores dos eventos ------------------------------------------
    
    def on_fechar_sobre_event(self, widget, event, data=None):
        # Se o retorno do gerenciador do sinal "delete_event" for "False",
        # o GTK disparará o sinal "destroy". Se for retornado "True" o
        # gerenciador de sinal "destroy" não tera um evento, assim a
        # janela não será fechada.
        
        print 'Botao(X) de fechar(sobre) pressionado.'
        return True

    def on_fechar_pizza_event(self, widget, event, data=None):
        # Se o retorno do gerenciador do sinal "delete_event" for "False",
        # o GTK disparará o sinal "destroy". Se for retornado "True" o
        # gerenciador de sinal "destroy" não tera um evento, assim a
        # janela não será fechada.
        
        print 'Botao(X) de fechar(pizza) pressionado.'
        return False

    def on_destruir_pizza_event(self, widget, data=None):
        # Fecha janela e encerra o programa
        print 'Sinal "destroy" disparado.'
        gtk.main_quit()

    # Metodos da classe --------------------------------------------------

    def iniciar(self):
        # Inicia toda aplicação.
        gtk.main()

if __name__ == '__main__':
    pizzagtk = PizzaGTK()
    pizzagtk.iniciar()
