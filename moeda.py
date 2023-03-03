import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

lista_moedas = ['USD', 'EUR']


def pegar_cotacao():
    pass


def selecionar_aquivo():
    pass


def atualizar_cotacao():
    pass



janela = tk.Tk()

janela.title('COTAÇÃO DE MOEDAS')

#ajustar a tela automáticamente

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 2], weight=1)


#cotação de uma moedas espesífica
label_cotacao_moeda = tk.Label(text='Sistema de Cotação de uma Moedas Específica', fg='#FFFFFF', borderwidth=2, relief='solid', bg='#000000')
label_cotacao_moeda.grid(row=0, column=0, columnspan=3, sticky='NSEW', padx=10, pady=10)#NSEW - norte, sul, leste, oeste

label_selecionar_cotacao = tk.Label(text='Selecionar Moeda:', anchor='e')
label_selecionar_cotacao.grid(row=1, column=0, columnspan=2, sticky='NSEW', padx=10, pady=10)#NSEW - norte, sul, leste, oeste

combobox_selecionar_moeda = ttk.Combobox(values=lista_moedas)
combobox_selecionar_moeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

label_selecionar_dia = tk.Label(text='Escolha o dia que deseja pegar a cotação:', anchor='e')
label_selecionar_dia.grid(row=2, column=0, columnspan=2, sticky='NSEW', padx=10, pady=10)#NSEW - norte, sul, leste, oeste

calendario_moeda = DateEntry(year=2023, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='NSEW')

label_texto_cotacao = tk.Label(text='')
label_texto_cotacao.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='NSEW')

botao_pegar_cotacao = tk.Button(text='PEGAR COTAÇÃO', command=pegar_cotacao)
botao_pegar_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky='NSWE')



#cotação de várias moedas
label_muiltipa_moeda = tk.Label(text='Sistema de Cotação de Multiplas Moedas', fg='#FFFFFF', borderwidth=2, relief='solid', bg='#000000')
label_muiltipa_moeda.grid(row=4, column=0, columnspan=3, sticky='NSEW', padx=10, pady=10)#NSEW - norte, sul, leste, oeste

label_selecionar_arquivo = tk.Label(text='Selecione um arquivo em Excel com as Moedas na Coluna A:')
label_selecionar_arquivo.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='NSWE')

botao_selecionar_arquivo = tk.Button(text='CLIQUE PARA SELECIONAR', command=selecionar_aquivo)
botao_selecionar_arquivo.grid(row=5, column=2, padx=10, pady=10, sticky='NSWE')

label_arquivo_selecionado = tk.Label(text='Nenhum arquivo selecionado', anchor='e')
label_arquivo_selecionado.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='NSWE')

label_data_inicial = tk.Label(text='DATA INICIAL:', anchor='e')
label_data_inicial.grid(row=7, column=0, padx=10, pady=10, sticky='NSWE')

label_data_final = tk.Label(text='DATA FINAL:', anchor='e')
label_data_final.grid(row=8, column=0, padx=10, pady=10, sticky='NSWE')

calendario_data_inicial = DateEntry(year=2023, locale='pt_br')
calendario_data_inicial.grid(row=7, column=1, padx=10, pady=10, sticky='NSWE')

calendario_data_final = DateEntry(year=2023, locale='pt_br')
calendario_data_final.grid(row=8, column=1, padx=10, pady=10, sticky='NSWE')

botao_atualizar_cotacao = tk.Button(text='ATUALIZAR COTAÇÂO', command=atualizar_cotacao)
botao_atualizar_cotacao.grid(row=9, column=0, padx=10, pady=10, sticky='NSWE')

label_atualizar_cotacao = tk.Label(text='')
label_atualizar_cotacao.grid(row=9, column=1, columnspan=2, padx=10, pady=10, sticky='NSWE')

botao_fechar = tk.Button(text='FECHAR', command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='NSWE')


janela.mainloop()