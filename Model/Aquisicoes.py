class Aquisicoes:
  def __init__ (self, data_aquisicao:str, metodo_pagamento: str):
    self.__data_aquisicao = data_aquisicao
    self.__metodo_pagamento = metodo_pagamento
    self.__usuario = []
    self.__jogo = []
  
  @property
  def data_aquisicao(self):
    return self.__data_aquisicao
  
  @data_aquisicao.setter
  def data_aquisicao(self, data_aquisicao):
    self.__data_aquisicao = data_aquisicao
  
  @property
  def metodo_pagamento(self):
    return self.__metodo_pagamento
  
  @metodo_pagamento.setter
  def metodo_pagamento(self, metodo_pagamento):
    self.__metodo_pagamento = data_aquisicao
  
  @property
  def usuario(self):
    return self.__jogo
  
  @property
  def jogo(self):
    return self.__usuario