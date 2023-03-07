import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
import pandas as pd
import requests
from datetime import datetime
import numpy as np


#API para a requisição de cotação
requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dic_moeda = requisicao.json()

lista_moedas = list(dic_moeda.keys())

#função requisição de moeda espesífica
def pegar_cotacao():
    moeda = combobox_selecionar_moeda.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:]
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano}{mes}{dia}_date={ano}{mes}{dia}'
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    valor_moeda = cotacao[0]['bid']
    label_texto_cotacao['text'] = f'A cotação da {moeda} no dia {data_cotacao} foi de: R$ {valor_moeda}'

# função selecionar o arquivo que vou colocar as cotações
def selecionar_aquivo():
    caminho_arquivo = askopenfilename(title='Selecione o Arquivo de Moeda')
    var_caminho_arquivo.set(caminho_arquivo)
    if caminho_arquivo:
        label_arquivo_selecionado['text'] = f'Arquivo Selecionado: {caminho_arquivo}'

#função que vai atualizar as cotações
def atualizar_cotacao():
    try:
        #ler o dataframe de moedas
        df = pd.read_excel(var_caminho_arquivo.get())
        moedas = df.iloc[:, 0]
        #pegar a data de inicios e fim cotações
        data_inicial = calendario_data_inicial.get()
        data_final = calendario_data_final.get()
        ano_inicial = data_inicial[-4:]
        mes_inicial = data_inicial[3:5]
        dia_inicial = data_inicial[:2]

        ano_final = data_final[-4:]
        mes_final = data_inicial[3:5]
        dia_final = data_inicial[:2]

        for moeda in moedas:
            link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?' \
                   f'start_date={ano_inicial}{mes_inicial}{dia_inicial}' \
                   f'_date={ano_final}{mes_final}{dia_final}'

            requisicao_moeda = requests.get(link)
            cotacoes = requisicao_moeda.json()
            for cotacoa in cotacoes:
                timestamp = int(cotacoa['timestamp'])
                bid = float(cotacoa['bid'])
                data = datetime.fromtimestamp(timestamp)
                data = data.strftime('%d/%m/%y')

                if data not in df:
                    print(data)
                    df[data] = np.nan

                df.loc[df.iloc[:, 0] == moeda, data] = bid

        df.to_excel('Teste2.xlsx')
        print(df)
        label_atualizar_cotacao['text'] = 'Arquivo Atualizado com Sucesso'

    except:
        label_atualizar_cotacao['text'] = 'Seleciona um arquivo Excel no formato correto'

janela = tk.Tk()

janela.title('COTAÇÃO DE MOEDAS')

#ajustar a tela automáticamente

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 4], weight=1)

#imagem da logo



# criação do visual da cotação de uma moedas espesífica
label_cotacao_moeda = tk.Label(text='Sistema de Cotação de uma Moedas Específica', fg='#FFFFFF', borderwidth=2, relief='solid', bg='#000000')
label_logo = tk.PhotoImage(file="icones/topo01.png")
label_cotacao_moeda.config(image=label_logo, compound='right')
label_cotacao_moeda.grid(row=0, column=0, columnspan=3, sticky='NSEW', padx=10, pady=10)#NSEW - norte, sul, leste, oeste


label_cotacao_moeda.config(image=label_logo, compound="right")

label_selecionar_cotacao = tk.Label(text='Selecionar Moeda:', anchor='e')
label_selecionar_cotacao.grid(row=1, column=0, columnspan=2, sticky='NSEW', padx=10, pady=10)#NSEW - norte, sul, leste, oeste

combobox_selecionar_moeda = ttk.Combobox(values=lista_moedas)
combobox_selecionar_moeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

label_selecionar_dia = tk.Label(text='Escolha o dia que deseja pegar a cotação:', anchor='e')
label_selecionar_dia.grid(row=2, column=0, columnspan=2, sticky='NSEW', padx=10, pady=10)#NSEW - norte, sul, leste, oeste

calendario_moeda = DateEntry(year=2023, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='NSEW')

label_texto_cotacao = tk.Label(text='', bg='#FFFFFF', borderwidth=2, relief='solid')
label_texto_cotacao.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='NSEW')

botao_pegar_cotacao = tk.Button(text='PEGAR COTAÇÃO', command=pegar_cotacao)
botao_pegar_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky='NSWE')



#criação do visual da cotação de várias moedas
label_muiltipa_moeda = tk.Label(text='Sistema de Cotação de Multiplas Moedas', fg='#FFFFFF', borderwidth=2, relief='solid', bg='#000000')
label_muiltipa_moeda.grid(row=4, column=0, columnspan=3, sticky='NSEW', padx=10, pady=10)#NSEW - norte, sul, leste, oeste

label_selecionar_arquivo = tk.Label(text='Selecione um arquivo em Excel com as Moedas na Coluna A:')
label_selecionar_arquivo.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='NSWE')

#váriavel do caminho arquivo
var_caminho_arquivo = tk.StringVar()

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

label_atualizar_cotacao = tk.Label(text='', bg='#FFFFFF', borderwidth=2, relief='solid')
label_atualizar_cotacao.grid(row=9, column=1, columnspan=2, padx=10, pady=10, sticky='NSWE')

botao_fechar = tk.Button(text='FECHAR', command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='NSWE')


janela.mainloop()
