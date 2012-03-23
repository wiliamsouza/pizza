# -*- coding: iso-8859-1 -*-
# -*- Mode: Python; py-indent-offset: 4 -*-

import gtk.glade



class TelefoneGTK:

    def __init__(self):
        # Carrega o arquivo ".glade".
        self.xml = gtk.glade.XML('glade/telefone.glade')

        # Conecta os sinais automaticamente.
        self.xml.signal_autoconnect(self)

        # Pega o di�logo principal
        self.telefone = self.xml.get_widget('telefone')

    # Manipuladores dos bot�es -------------------------------------------

    def on_salvar_clicked(self, button):
        # Salva telefone
        print 'Bot�o salvar pressionado'

    def on_fechar_clicked(self, button):
        # Enconde a janela.
        print 'Bot�o fechar pressionado'
        self.telefone.hide()

    # Manipuladores dos eventos ------------------------------------------

    def on_fechar_event(self, widget, event, data=None):
        # Se o retorno do gerenciador do sinal "delete_event" for "False",
        # o GTK disparar� o sinal "destroy". Se for retornado "True" o
        # gerenciador de sinal "destroy" n�o tera um evento, assim a
        # janela n�o ser� fechada.
        
        print 'Botao(X) de fechar(telefone) pressionado.'
        widget.hide()
        return True

    # Metodos da classe --------------------------------------------------
    
    def mostrar_janela(self):
        # Mostra o di�logo
        self.telefone.show()

if __name__ == '__main__':
    print 'Esta classe n�o pode ser chamada desta forma.'
