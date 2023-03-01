import tkinter as tk

janela = tk.Tk()

janela.title('COTAÇÃO DE MOEDAS')

mensagem = tk.Label(text='Sistema de Busca de Cotação de Moedas', fg='white', bg='black', width=35, height=5)
mensagem.pack()

mensagem = tk.Label(text='Selecione a moeda desejada')
mensagem.pack()

moeda = tk.Entry()
moeda.pack()

janela.mainloop()