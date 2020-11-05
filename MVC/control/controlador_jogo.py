from MVC.model.jogo import Jogo
from MVC.view.tela_jogo import TelaJogo

class ControladorJogo:
  def __init__(self, controlador_biblioteca):
    #if isinstance (controlador_biblioteca, ControladorBiblioteca): 
      self.__controlador_biblioteca = controlador_biblioteca
      self.__tela = TelaJogo(self)
      self.__jogos = []

   def abre_tela(self):
    #evocaco do método do menu criado na classe de tela 
    [opcao, genero, nome, ano_lancamento, horas_jogadas, total_trofeus, trofeus_acumulados, jogo_finalizado] = self.__tela.tela_opcoes()
    
    if opcao == 1:
      self.incluir_jogo(genero, nome, ano_lancamento, horas_jogadas, total_trofeus, trofeus_acumulados, jogo_finalizado)
    elif opcao == 2:
      self.excluir_jogo(nome)
    elif opcao == 3: 
      self.lista_jogos()

    # essa função serve para instanciar um objeto jogo e colocar na lista de jogos
  def incluir_jogo(self, genero: str, nome: str, ano_lancamento: int, horas_jogadas: int, total_trofeus: int, trofeus_acumulados: int, jogo_finalizado: bool, multiplayer: bool, preco: float):
    self.__jogos.append(Jogo(genero,nome,ano_lancamento,horas_jogadas, total_trofeus, trofeus_acumulados, jogo_finalizado, multiplayer, preco))

    # essa funçao percorre toda a lista de jogo para localizar o registro com o nome que foi passado como parametro. quando acha esse registro, o objeto é removido
  def excluir_jogo(self, nome: str):
    if isinstance (nome, str):
      for nome in self.__nomes:
        if jogo.nome = nome:
          self.__nome.remove(jogo)

  #essa funcao retorna a lista de jogos
  def listar_jogos(self):
    lista_jogos = []
    for jogo in self.__jogos:
      lista_jogos.append(jogo.nome)
      #invocação do método próprio da tela para exibição da lista ao invés do print. O método recebe uma lista de strings. Ela incia vazia e a cada iteração é adicionado o jogo.nome
    self.__tela.exibir_tela(lista_jogos)

  # percorrer a lista e retornar o objeto de jogo cujo parametro nome seja igual ao parametro nome da funcao de listagem
  def listar_jogo_por_nome(self, nome: str):
    if isinstance(nome, str):
      for jogo in self.__jogos:
        if jogo.nome == nome
          return jogo