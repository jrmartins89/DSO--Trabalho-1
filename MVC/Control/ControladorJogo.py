class ControladorJogo:
  def __init__(self, controlador_biblioteca: ControladorBiblioteca):
    self.controlador_biblioteca = controlador_biblioteca
  
  def incluir_jogo(self, genero: str, ano_lancamento: str, horas_jogadas: int, total_trofeus: int, trofeus_acumulados: int, jogo_finalizado: boolean, multiplayer: boolean, preco: float):
    self.__genero = genero
    self.__ano_lancamento = ano_lancamento
    self.__horas_jogadas = horas_jogadas
    self.__total_trofeus = total_trofeus
    self.__trofeus_acumulados = trofeus_acumulados
    self.__jogo_finalizado = jogo_finalizado
    self.__multiplayer = multiplayer
    self.__preco = preco
    self.__controlador_biblioteca = []
  
  # def excluir_jogo (self, nome: str)

  # def listar_jogo_horas(nome: str)

  # def listar_trofeus_jogo(nome: str)

  # def listar_jogos_finalizados(self)

  # def listar_jogos_multiplayer(self)

  # def listar_jogos_single_player(self)

  