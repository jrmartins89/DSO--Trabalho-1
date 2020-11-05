class Jogo:
  def __init__(self, genero: str, nome: str, ano_lancamento: int, horas_jogadas: int, preco: float, total_trofeus: int, finalizado: bool, multiplayer: bool):
    if isinstance(nome, str):
      self.__genero = genero
      self.__nome = nome
      self.__ano_lancamento = ano_lancamento
      self.__horas_jogadas = horas_jogadas
      self.__preco = preco
      self.__total_trofeus = total_trofeus
      self.__finalizado = finalizado
      self.__multiplayer = multiplayer
      self.__aquisicoes = []

  @property
  def genero(self):
    return self.__genero

  @genero.setter
  def genero(self, genero: str):
    if isinstance(genero, str):
      self.__genero = genero

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self,nome: str):
    if isinstance(nome, str):
      self.__nome = nome

  @property
  def ano_lancamento(self):
    return self.__ano_lancamento

  @ano_lancamento.setter
  def ano_lancamento(self, ano_lancamento: int):
    if isinstance(ano_lancamento, int):
      self.__ano_lancamento = ano_lancamento

  @property
  def horas_jogadas(self):
    return self.__horas_jogadas

  @horas_jogadas.setter
  def horas_jogadas(self, horas_jogadas: int):
    if isinstance(horas_jogadas, int):
      self.__horas_jogadas = horas_jogadas

  @property
  def preco(self):
    return self.__preco

  @preco.setter
  def preco(self, preco: float):
    if isinstance(preco, float):
      self.__preco  = preco

  @property
  def total_trofeus(self):
    return self.__total_trofeus

  @total_trofeus.setter
  def total_trofeus(self, total_trofeus: int):
    if isinstance(total_trofeus, float):
      self.__total_trofeus = total_trofeus

  @property
  def finalizado(self):
    return self.__finalizado

  @finalizado.setter
  def finalizado(self, finalizado:bool):
    if isinstance(finalizado, bool):
      self.__finalizado = finalizado

  @property
  def multiplayer(self):
    return self.__multiplayer

  @multiplayer.setter
  def multiplayer(self, multiplayer: bool):
    if isinstance(multiplayer,bool):
      self.__multiplayer = multiplayer
  
  @property
  def aquisicoes(self):
    return self.__aquisicoes
  
  