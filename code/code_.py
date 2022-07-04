from tkinter import *

class frontEnd():
    def __init__(self):
        self.front = Tk()

        self.primera_Tela_Config()
        self.primera_Tela_Widgets()

        self.front.mainloop()

    def primera_Tela_Config(self):
        self.front.geometry('500x600')
        self.front.resizable(0, 0)
        self.front.config(background='gray')
    
    def primera_Tela_Widgets(self):
        ###creating###
        self.powered_label = Label(
            self.front,
            text='Powered By Higor Ramos',
            bg='gray'
        )
        self.link_label = Label(
            self.front,
            text='Link do YouTube:',
            bg='gray'
        )
        self.link_video_Entry = Entry(self.front)

        ###inserting###
        self.powered_label.place(
            x=170,
            y=580
        )
        self.link_label.place(
            x=70,
            y=280
        )
        self.link_video_Entry.place(
            x=70,
            y=300,
            width=350,
            height=30
        )

frontEnd()
