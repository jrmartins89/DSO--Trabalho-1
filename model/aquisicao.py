from MVC.model.usuario import Usuario
from MVC.model.jogo import Jogo

class Aquisicao:
  def __init__ (self, usuario: Usuario, jogo: Jogo, data_aquisicao:str, metodo_pagamento: str):
    self.__usuario = usuario
    self.__jogo = jogo
    self.__data_aquisicao = data_aquisicao
    self.__metodo_pagamento = metodo_pagamento
  
  @property
  def data_aquisicao(self):
    return self.__data_aquisicao
  
  @data_aquisicao.setter
  def data_aquisicao(self, data_aquisicao: str):
    if isinstance(data_aquisicao, str):
      self.__data_aquisicao = data_aquisicao
  
  @property
  def metodo_pagamento(self):
    return self.__metodo_pagamento
  
  @metodo_pagamento.setter
  def metodo_pagamento(self, metodo_pagamento: str):
    if isinstance (metodo_pagamento, str):
      self.__metodo_pagamento = metodo_pagamento
  
  @property
  def usuario(self):
    return self.__usuario
  
  @property
  def jogo(self):
    return self.__jogo
