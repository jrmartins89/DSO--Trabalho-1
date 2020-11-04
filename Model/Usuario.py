class Usuario:
def __init__(self, nome: str, email: str, id_usuario: str):
    self.__nome = nome
    self.__email = email
    self.__id_usuario = id_usuario
    self.__aquisicoes = []

  @property
  def nome(self):
    return self.__nome
  
  @nome.setter
  def nome(self, nome):
    self.__nome = nome
  
  @property
  def email(self):
    return self.__email
  
  @email.setter
  def email(self, email):
    self.__email = email
  
  @property
  def aquisicoes(self):
    return self.__aquisicoes