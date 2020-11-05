from tela import Tela

Class TelaAquisicao(Tela):

def __init__(self, controlador):
    self.__controlador = controlador
# # tratar quando o usuário não digitar nem 1,2,3 e opção 0 para voltar para o menu principal
def tela_opcoes(self):
    print("Bem vindo a Biblioteca Gamer!")
    print("Escolha uma opção:")
    print("1: efetuar aquisição")
    print("2: listar aquisições")
    opcao = int(input("opção:"))
    id = None
    nome = None

    if opcao == 1 or opcao == 2:
      id_usuario = input(str("id do usuário: "))
      nome = input("nome do jogo:")

    return [opcao, id_usuario, nome]

  def mostrar_msg_de_erro(self, msg: str):
    print(msg)