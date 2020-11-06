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
    [opcao, nome, genero, ano_lancamento, horas_jogadas, total_trofeus] = self.__tela.tela_opcoes()
    
    if opcao == 1:
      self.incluir_jogo(nome, genero, ano_lancamento, horas_jogadas, total_trofeus)
    elif opcao == 2:
      self.excluir_jogo(nome)
    else: 
      self.listar_jogos()

    # essa função serve para instanciar um objeto jogo e colocar na lista de jogos
  def incluir_jogo(self, nome: str, genero: str, ano_lancamento: int, horas_jogadas: int, total_trofeus: int):
    self.__jogos.append(Jogo(nome, genero, ano_lancamento, horas_jogadas,total_trofeus))
    print("Jogo cadastrado com sucesso!")

    # essa funçao percorre toda a lista de jogo para localizar o registro com o nome que foi passado como parametro. quando acha esse registro, o objeto é removido
  def excluir_jogo(self, nome: str):
    if isinstance (nome, str):
      for jogos in self.__jogos:
        if jogos.nome == nome:
            self.__jogos.remove(jogos)
            print("Jogo excluído com sucesso!")

  #essa funcao retorna a lista de jogos
  def listar_jogos(self):
    lista_jogos = []
    print("listando jogos da biblioteca...")
    for jogos in self.__jogos:
      lista_jogos.append(jogos.nome)
      #invocação do método próprio da tela para exibição da lista ao invés do print. O método recebe uma lista de strings. Ela incia vazia e a cada iteração é adicionado o jogo.nome
    self.__tela.mostra_lista_str(lista_jogos)

  # percorrer a lista e retornar o objeto de jogo cujo parametro nome seja igual ao parametro nome da funcao de listagem
  def listar_jogo_por_nome(self, nome: str):
    if isinstance(nome, str):
      for jogos in self.__jogos:
        if jogos.nome == nome:
          return jogos