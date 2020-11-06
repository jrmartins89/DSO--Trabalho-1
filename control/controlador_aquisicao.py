from MVC.view.tela_aquisicao import TelaAquisicao
from MVC.model.aquisicao import Aquisicao

class ControladorAquisicao:


    def __init__(self, controlador_biblioteca):
        self.__controlador_biblioteca = controlador_biblioteca
        self.__tela = TelaAquisicao(self)
        self.__aquisicoes = []


    def abre_tela(self):
        [opcao, id_usuario , nome, forma_pagamento, preco_compra] = self.__tela.tela_opcoes()
        if opcao == 1:
            self.efetuar_aquisicao(id_usuario, nome,forma_pagamento, preco_compra)
        elif opcao == 2:
            self.listar_aquisicoes()

    # o controlador biblioteca sao privados porque nessa classe de controlador de aquisiçao não há getter, entao o acesso tem que ser de forma privada
    
    def efetuar_aquisicao(self, id_usuario: str, jogo: str, foma_pagamento: str, preco_compra: float):
      usuario = self.__controlador_biblioteca.controlador_usuario.listar_usuario_por_id(id_usuario)
      jogo = self.__controlador_biblioteca.controlador_jogo.listar_jogo_por_nome(jogo)
      self.__aquisicoes.append(Aquisicao(usuario,jogo,"11/05/2020",foma_pagamento,preco_compra))
      print("jogo adquirido!")



    def listar_aquisicoes(self):
        lista_aquisicoes = []
        for aquisicoes in self.__aquisicoes:
          lista_aquisicoes.append(aquisicoes.jogo.nome)
        self.__tela.mostra_lista_str(lista_aquisicoes)
