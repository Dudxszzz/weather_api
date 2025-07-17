import tkinter as tk
from tkinter import *

def captura_texto(event=None):
    texto_digitado = bar.get()
    print("Texto digitado:", texto_digitado)

    bar.delete(0, tk.END) #limpa o campo de texto após o tenter

root = tk.Tk()
root.title("Weather API")
root.geometry("500x500")

title = tk.Label(root, text="Weather", font=("Arial", 40))
title.pack(pady=25)

text = tk.Label(root, text="Saiba a previsão do tempo de qualquer lugar a qualquer hora com o Weather", font=(8))
text.pack(pady=5)

bar = tk.Entry(root, width=40) #criando campo de texto
bar.pack(pady=10)

bar.bind("<Return>", captura_texto) #vincula o evento (Enter) a função captura_texto()

# Botão para captura de texto
button = tk.Button(root, text="Captura de texto", command=captura_texto)
button.pack(pady=5)

root.mainloop()