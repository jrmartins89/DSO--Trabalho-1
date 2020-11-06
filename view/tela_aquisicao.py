from MVC.view.tela import Tela

class TelaAquisicao(Tela):

  def __init__(self, controlador_aquisicao):
    self.__controlador_aquisicao = controlador_aquisicao
# # tratar quando o usuário não digitar nem 1,2,3 e opção 0 para voltar para o menu principal
  def mostra_lista_str(self, lista: []):
        for elem in lista:
            print(elem)
            
  def tela_opcoes(self):
    print("Bem vindo a Biblioteca Gamer!")
    print("Escolha uma opção:")
    print("1: Efetuar aquisição")
    print("2: Listar aquisições")
    opcao = int(input("Escolha a opção: "))
    id_usuario = None
    nome = None
    preco_compra = None
    forma_pagamento = None
    if opcao == 1:
      id_usuario = input("Insira o id do usuário: ")
      nome = input("Insira o nome do jogo: ")
      preco_compra = float(input("Insira o preco do jogo: "))
      forma_pagamento = input("Insira a forma de pagamento: ")
      return [opcao, id_usuario, nome, preco_compra, forma_pagamento]

    elif opcao == 2:
      id_usuario = None
      nome = None
      preco_compra = None
      forma_pagamento = None
      return [opcao, id_usuario, nome, forma_pagamento, preco_compra]