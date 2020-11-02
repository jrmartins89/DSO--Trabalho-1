Class Usuario:
  def __init__(self, nome: str, email: str, id_usuario: str):
    self.__nome = nome
    self.__email = email
    self.__id_usuario = id_usuario

  @property
  def nome(self):
    return self.__nome
  
  @nome.setter
  def nome(nome):
    self.__nome = nome
  
  @property
  def email(self):
    return self.__email
  
  @email.setter
  def email(email):
    self.__email = email

