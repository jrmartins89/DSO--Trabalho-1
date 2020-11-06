from MVC.view.tela_biblioteca import TelaBiblioteca
from MVC.control.controlador_jogo import ControladorJogo
from MVC.control.controlador_usuario import ControladorUsuario
from MVC.control.controlador_aquisicao import ControladorAquisicao

class ControladorBiblioteca:
  def __init__(self):
    #o controlador da biblioteca cria a própria tela e os demais controladores que ele acessará.
    self.__tela = TelaBiblioteca(self)
    self.__controlador_usuario = ControladorUsuario(self)
    self.__controlador_jogo = ControladorJogo(self)
    self.__controlador_aquisicao = ControladorAquisicao(self)
  
  # para chamar a tela de usuarios é necessário pensar que o controlador da biblioteca conhece o controlador de usuários. Nesse caso é possível chamar o controlador de amigos porque dentro dele há um método que chama a tela de amigos. O raciocínio é válido para as demais opções

  #criando um laço de repeticao

  def abre_tela(self):
    while True: 
      opcao = self.__tela.tela_opcoes()
      if opcao == 1:
        self.__controlador_usuario.abre_tela()
      
      if opcao == 2:
        self.__controlador_jogo.abre_tela()
      
      if opcao == 3:
        self.__controlador_aquisicao.abre_tela()
      

  
  #os getters sao necessários nessa classe do controlador da biblioteca porque o controlador de aquisicoes precisa acessar os outros controladores, no caso o controlador de usuarios e controlador de jogos. 
  @property
  def controlador_usuario(self):
    return self.__controlador_usuario
  
  @property
  def controlador_jogo(self):
    return self.__controlador_jogo
  
  @property
  def controlador_aquisicao(self):
    return self.__controlador_aquisicao