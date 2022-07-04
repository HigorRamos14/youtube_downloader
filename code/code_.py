from tkinter import *
from pytube import YouTube

class youtube_Downloader():
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
            text='Created By Higor Ramos',
            bg='gray'
        )
        self.link_label = Label(
            self.front,
            text='Link do YouTube:',
            bg='gray'
        )
        self.link_video_Entry = Entry(self.front)

        self.baixar_Link_Button = Button(
            self.front,
            text='Baixar',
            command=self.baixar_video,
            height=3,
            width=15
        )

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
        self.baixar_Link_Button.place(
            x=185,
            y=410
        )

    def janela_de_mensagem(self):
        self.jan_de_aviso = Tk()

        self.jan_de_aviso.geometry('210x80')

        self.link_invalido = Label(
            self.jan_de_aviso,
            text='Link inválido, insira um link válido'
        )
        self.link_invalido.pack()

        self.ok_button = Button(
            self.jan_de_aviso,
            text='Ok',
            command=self.close_mesage
        )
        self.ok_button.pack()

        self.jan_de_aviso.mainloop()
    
    def close_mesage(self):
        self.jan_de_aviso.destroy()

    def baixar_video(self):
        try:
            self.jan_de_aviso.destroy()

        except:
            pass
        
        self.url = self.link_video_Entry.get()

        if self.url == '' :
            self.janela_de_mensagem()

        else:
            try:
                self.youtube = YouTube(self.url)
                self.video = self.youtube.streams.get_highest_resolution()
                self.video.download()

            except:
                self.janela_de_mensagem()
    
youtube_Downloader()
