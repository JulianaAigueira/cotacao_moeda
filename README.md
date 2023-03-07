# cotacao_moeda

 Para a realização desse projeto utilizei Python para parte do back end e para o visual a biblioteca Tkinter. Para fazer a requisição da cotação utilizei uma API.
 Segue o Link da API: https://docs.awesomeapi.com.br/api-de-moedas

 Sistema onde usuário vai poder escolher a moeda específica e o dia para fazer a cotação em tempo real. Ao clicar no botão 'PEGAR COTAÇÃO' vai ser exibido em um Label a resposta.
 
 O sistema também oferece fazer a cotação de grupos de moedas. O usuário tem que escolher um arquivo xlsx para atualizar esse grupo de moedas, ao escolher o arquivo o usuário pode escolher a data inicial e final da cotação que deseja. Vai clicar no botão 'ATUALIZAR A COTAÇÂO' e o arquivo selecionado será atualizado com as informações requisitadas.
  
 Tela do sistema:
 
 Ele tem dois tipos de cotação. Cotação por moeda específica e por Multiplas moedas.
 
 ![sistema](https://user-images.githubusercontent.com/121833579/223447645-8e86d48f-690e-49bf-bcbf-17634cf3d6fa.png)

 No Combobox tem uma lista de moedas que requisitei da API.
 É só escolher a moeda que deseja fazer a cotação.
 
 ![cotacao_especifica](https://user-images.githubusercontent.com/121833579/223449558-ea1caf55-2762-4a8d-a54f-505037a90e30.png)
 
 A baixo do Combobox tem um calendário (DateEntry) para escolher a data que desejar.
 
 ![data](https://user-images.githubusercontent.com/121833579/223451906-0caad0ae-fd5b-41eb-b407-53763f3ebad4.png)

 Ao clicar no botão 'PEGAR COTAÇÃO' será exibido no Label a cotação da moeda e do dia específico.

![cotação moeda especifica](https://user-images.githubusercontent.com/121833579/223452512-83bcbcea-30c4-48e1-9f1e-bafea5c93cfa.png)

Para fazer a Cotação de Multiplas Moedas, primeiro o usuário vai ter que escolher um arquivo xlsx.
Ao clicar no botão 'CLIQUE PARA SELECIONAR' abrirar uma janela pra escolher o arquivo.

![selecionar o arquivo](https://user-images.githubusercontent.com/121833579/223453303-ecac1439-f125-4166-8a32-c724380d4585.png) ![arquivo](https://user-images.githubusercontent.com/121833579/223453826-02fa31ad-f80b-4e21-a1f5-62c88d20d3bd.png)

Caso o aquivo selecionado não for o correto será exibido uma mensagem.

![aviso de arquivo errado](https://user-images.githubusercontent.com/121833579/223454700-dd3eba3e-534a-4850-b3b5-47bf3d8db322.png)

Arquivo selecionado corretamente e datas iniciais e finais escolhidas ao clicar no botão 'ATUALIZAR COTAÇÃO' será exibido em um Label uma mensagem de 'Arquivo Atualizado com sucesso'.
 
 ![arquivo atualizado](https://user-images.githubusercontent.com/121833579/223455580-8514b6e2-7b3a-4db7-822a-01fbedc2d3ba.png)

 O arquivo atualizado.
 
 ![image](https://user-images.githubusercontent.com/121833579/223456320-c4212298-c901-4b39-9b20-06baecccd777.png)

Para fechar o sistema é só clicar no botão 'FECHAR.

![fechar programa](https://user-images.githubusercontent.com/121833579/223456674-8d13f879-1bd9-4c6a-a511-9019cf46e703.png)


 

 

