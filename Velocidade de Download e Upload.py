from tkinter import Tk
from tkinter import *
from speedtest import Speedtest


def analise():
    speed_test = Speedtest()  # Chama o Speedtest
    download = speed_test.download()  # Aciona o teste de velocidade de Download
    upload = speed_test.upload()  # Aciona o teste de velocidade de Upload

    download_speed = round(download / (10**6), 2)  # Converção para Mbps
    down_label.config(text="Velocidade de Download: " +
                      str(download_speed) + " Mbps")  # Concatenação de string com resultado

    upload_speed = round(upload / (10**6), 2)  # Converção para Mbps
    up_label.config(text="Velocidade de Upload: " +
                    str(upload_speed) + " Mbps")  # Concatenação de string com resultado


root = Tk()  # Inicia o TKinter
root.title("Internet Speed Tracker")  # Título da janela
root.geometry('600x500')  # Tamanho da janela

button = Button(root, text="Excutar Análise", width=30,
                command=analise).pack()   # Botão Excutar Análise

down_label = Label(root, text="")
down_label.pack()
up_label = Label(root, text="")
up_label.pack()
ping_label = Label(root, text="")
ping_label.pack()


root.mainloop()
