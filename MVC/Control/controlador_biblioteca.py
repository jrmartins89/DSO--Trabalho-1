class ControladorBiblioteca:
  def __init__(self):
    #o controlador da biblioteca cria a própria tela e os demais controladores que ele acessará.
    self.__tela = TelaBiblioteca(self)
    self.__controlador_usuario = ControladorUsuario(self)
    self.__controlador_jogo = ContoladorJogo(self)
    self.__controlador_aquisicao = ControladorAquisicao(self)
  
  def abre_tela(self):
    pass
  
  #os getters sao necessários nessa classe do controlador da biblioteca porque o controlador de aquisicoes precisa acessar os outros controladores, no caso o controlador de usuarios e controlador de jogos. 
  @property
  def controlador_usuario(self):
    return self.__controlador_usuario
  
  @property
  def controlador_jogo(self):
    return self.__controladro_jogo
  
  @property
  def controlador_aquisicao(self):
    return self.__controlador_aquisicao

  #def controlador_jogo(self):

  #def controlador_usuario(self):

