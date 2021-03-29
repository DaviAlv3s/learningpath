import random
import PySimpleGUI as sg



                                        ###############IMPORTANTE##############
class ChuteONumero:          #CRIAÇÃO DA CLASSE >>>>>> INSTANCIAR A CLASSE LOGO EM SEQUENCIA ( LINHA 36 e 37)#
    def __init__ (self):
        self.valor_aleatorio = 0                ###############IMPORTANTE##############
        self.valor_minimo = 1                   #FAZER O USO DA self. NAS VARIAVEIS#
        self.valor_maximo = 100                 #TORNAM AS VARIVEIS ACESSIVEL#
        self.tentar_novamente = True            #EM TODOS OS METODOS DA CLASSE#

        #LAYOUT
        self.layout = [
            [sg.Text("Seu chute", size=(20,0))],
            [sg.Input(size=(5,0), key="ValorChute")],
            [sg.Button("CHUTAR!",size=(10,2))], [sg.Button("EXIT", size=(10,2))],         #[sg.Button("{:>50}".format("CHUTAR!"))],
            [sg.Output(size=(40,10))],
            [sg.Checkbox('My Checkbox', default=True)]

        ]
    def Iniciar(self):
        #CRIAR JANELA
        self.janela = sg.Window("Chute o Número!",layout = self.layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # LER VALORES DA JANELA
                self.evento, self.valores = self.janela.Read()
                # CONDICIONAL PARA FECHAMENTO CORRETO DA JANELA
                if self.evento == sg.WIN_CLOSED or self.evento == "EXIT":
                    break
                # TRATAR OS VALORES LIDOS NA JANELA
                if self.evento == "CHUTAR!":
                    self.valor_do_chute = self.valores["ValorChute"]
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print("Chute um valor MENOR!")
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print("Chute um valor MAIOR!")
                            break
                        if int(self.valor_do_chute) == int(self.valor_aleatorio):
                            self.tentar_novamente = False
                            print("Parabéns você acertou!")
                            break
        except:
            print('O programa aceita apenas números inteiros!')
            self.Iniciar()

    def PedirValorAleatorio(self):
        self.valor_do_chute = input("Chute um número: ")

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)




chute = ChuteONumero()    #INSTANCINDO A CLASSE
chute.Iniciar()           #INICIALIZANDO A CLASSE
