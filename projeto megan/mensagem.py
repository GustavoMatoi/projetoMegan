
class Mensagem: 
    def __init__(self):
        self.horario = ''
        self.texto = ''
        self.tipo = ''

    def montarMensagem(self):
        with open('mensagens.txt', 'a') as arquivoDeMensagens:
            arquivoDeMensagens.write(self.horario, " ", self.texto)
        