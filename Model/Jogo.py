Class Jogo:
  def __init__(self, genero: str, nome: str, ano_lancamento: int, horas_jogadas: int, preco: float, total_trofeus: int, finalizado: bool, multiplayer: bool, preco: float):
    self.__genero = genero
    self.__nome = nome
    self.__ano_lancamento = ano_lancamento
    self.__horas_jogadas = horas_jogadas
    self.__preco = preco
    self.__total_trofeus = total_trofeus
    self.__finalizado = finalizado
    self.__multiplayer = multiplayer

  @property
  def genero(self):
    return self.__genero

  @genero.setter
  def genero(genero):
    self.__genero = genero

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(nome):
    self.__nome = nome

  @property
  def ano_lancamento(self):
    return self.__ano_lancamento

  @ano_lancamento.setter
  def ano_lancamento(ano_lancamento):
    self.__ano_lancamento = ano_lancamento

  @property
  def horas_jogadas(self):
    return self.__horas_jogadas

  @horas_jogadas.setter
  def horas_jogadas(horas_jogadas):
    self.__horas_jogadas = horas_jogadas

  @property
  def preco(self):
    return self.__preco

  @preco.setter
  def preco(preco):
    return self.__preco

  @property
  def total_trofeus(self):
    return self.__total_trofeus

  @total_trofeus.setter
  def total_trofeus(total_trofeus):
    self.__total_trofeus = total_trofeus

  @property
  def finalizado(self):
    return self.__finalizado

  @finalizado.setter
  def finalizado(finalizado):
    self.__finalizado = finalizado

  @property
  def multiplayer(self):
    return self.__multiplayer

  @multiplayer.setter
  def multiplayer(multiplayer):
    self.__multiplayer = multiplayer