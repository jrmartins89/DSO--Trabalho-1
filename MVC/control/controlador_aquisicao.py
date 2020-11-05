from MVC.View.tela_aquisicao import TelaAquisicao
from MVC.Model.aquisicao import Aquisicao

Class ControladorAquisicao:


    def __init__(self, controlador_biblioteca):
        self.__controlador_biblioteca = controlador_biblioteca
        self.__tela = TelaAquisicao(self)
        self.__aquisicoes = []


    def abre_tela(self):
        [opcao, jogo, usuario] = self.__tela.tela_opcoes()


        if opcao == 1:
            self.efetuar_aquisicao(usuario, jogo)
        elif opcao == 2:
            self.listar_aquisicoes()


    def efetuar_aquisicao():
        try:
            usuario =
            self.__controlador.biblioteca.controlador_usario.listar_usuario_por_id(id)
            jogo =
            self.__controlador_biblioteca.controlador_jogo.listra_jogo_por_nome(nome)
        except Exception:
            self.__tela.mostrar_msg_de_erro("Usuário ou jogo não encontrado")
        else:
            self.__aquisicoes.append(Aquisicao(usuario, jogo, data_aquisicao, metodo_pagamento))


    def listar_aquisicoes():
        lista_aquisicoes = []
        for aquisicao in self__aquisicoes:
            lista_aquisicoes.append(aquisicao.usuario.id + aquisicao.jogo.nome + aquisicao.data_aquisicao)
            self.__tela.exibe_lista_str(lista_aquisicoes)
