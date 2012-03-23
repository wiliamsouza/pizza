# -*- coding: iso-8859-1 -*-
# -*- Mode: Python; py-indent-offset: 4 -*-

import gtk.glade



class SaborGTK:

    def __init__(self):
        # Carrega o arquivo ".glade".
        self.xml = gtk.glade.XML('glade/sabor.glade')

        # Conecta os sinais automaticamente.
        self.xml.signal_autoconnect(self)

        # Pega o di�logo principal
        self.sabor = self.xml.get_widget('sabor')

    # Manipuladores dos bot�es -------------------------------------------

    def on_salvar_clicked(self, button):
        # Salva sabor
        print 'Bot�o salvar pressionado'

    def on_fechar_clicked(self, button):
        # Enconde a janela.
        print 'Bot�o fechar pressionado'
        self.sabor.hide()

    # Manipuladores dos eventos ------------------------------------------

    def on_fechar_event(self, widget, event, data=None):
        # Se o retorno do gerenciador do sinal "delete_event" for "False",
        # o GTK disparar� o sinal "destroy". Se for retornado "True" o
        # gerenciador de sinal "destroy" n�o tera um evento, assim a
        # janela n�o ser� fechada.
        
        print 'Botao(X) de fechar(sabor) pressionado.'
        widget.hide()
        return True

    # Metodos da classe --------------------------------------------------
    
    def mostrar_janela(self):
        # Mostra o di�logo
        self.sabor.show()

if __name__ == '__main__':
    print 'Esta classe n�o pode ser chamada desta forma.'
