import tkinter as tk

janela = tk.Tk()

var_promocoes = tk.IntVar()
chekbox_promocoes = tk.Checkbutton(text='Deseja receber e-mail promocionais?', variable=var_promocoes)
chekbox_promocoes.grid(row=0, column=0)

var_politicas = tk.IntVar()
checkbox_politicas = tk.Checkbutton(text='Aceitar Termos de Uso e Políticas de Privacidade', variable=var_politicas)
checkbox_politicas.grid(row=1, column=0)


def enviar():
    if var_promocoes.get():
        print(f'Usuário deseja receber promoções')
    else:
        print(f'Usuário NÃO deseja receber promoções')
    if var_politicas.get():
        print(f'Usuário concordou com Termos de Uso e Políticas de Privacidade')
    else:
        print(f'Usuário NÃO concordou')


botao_enviar = tk.Button(text='Enviar', command=enviar)
botao_enviar.grid(row=2, column=0)


janela.mainloop()
