from tkinter import *

root = Tk()
antecedentes = []

class Funcs():

  def gato(self):
    antecedentes.append('Miau')
    print('Miau')

  def cachorro(self):
    antecedentes.append('Auau')
    print('Auau')

  def history(self):
      global antecedentes
      if antecedentes == []:
        print("Sem histórico para mostrar.")
      else:
        print('Histórico:')
        for i in antecedentes:
          print(i)


class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets()
        root.mainloop()

    def tela(self):
        self.root.title("Questão 1")
        self.root.geometry("350x300")
        self.root.resizable(True, True)
        self.root.configure(background='grey')
        self.root.maxsize(width=500,height=400)
        self.root.minsize(width=500,height=400)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=1, bg='grey')
        self.frame_1.place(relx=0.01, rely=0.01, relwidth=0.99, relheight=0.99)

    def widgets(self):
        self.bt_gato = Button(self.frame_1, text="Input 1 - GATO", border=2, bg='#ee1515', fg='white', command=self.gato)
        self.bt_gato.configure()
        self.bt_gato.place(relx=0.1, rely=0.05, relheight=0.1, relwidth=0.8)

        self.bt_cachorro = Button(self.frame_1, text="Input 2 - CACHORRO", border=2, bg='#ee1515', fg='white', command=self.cachorro)
        self.bt_cachorro.configure()
        self.bt_cachorro.place(relx=0.1, rely=0.2, relheight=0.1, relwidth=0.8)

        self.bt_hist = Button(self.frame_1, text="Histórico", border=2, bg='#ee1515', fg='white', command=self.history)
        self.bt_hist.configure()
        self.bt_hist.place(relx=0.1, rely=0.35, relheight=0.1, relwidth=0.8)

        self.label_questao = Label(self.frame_1, height=10, width=69, wraplength=200, text=" Questão 1 - Desenvolva uma solução em Python que receba input “1” para “GATO” e “2” para “CACHORRO”. Quando selecionada a opção “1”, o output deve ser “Miau”. Quando o a opção for “2”, o output deve ser “Auau”. Se o input for “histórico”, o output deve apresentar a lista de execuções do software. ")
        self.label_questao.place(rely=0.5)

Application()

