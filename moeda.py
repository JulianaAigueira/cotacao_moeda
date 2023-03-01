import tkinter as tk

janela = tk.Tk()

janela.title('COTAÇÃO DE MOEDAS')

#ajustar a tela automáticamente

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text='Sistema de Busca de Cotação de Moedas', fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky='NSEW')#NSEW - norte, sul, leste, oeste

mensagem2 = tk.Label(text='Selecione a moeda desejada')
mensagem2.grid(row=1, column=0)

moeda = tk.Entry()
moeda.grid(row=1, column=1)

janela.mainloop()