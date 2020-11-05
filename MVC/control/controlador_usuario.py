from MVC.model.usuario import Usuario
from MVC.view.tela_usuario import TelaUsuario

class ControladorUsuario:
  def __init__(self, controlador_biblioteca: ControladorBiblioteca):
    if isinstance (controlador_biblioteca, ControladorBiblioteca):
      self.__controlador_biblioteca = controlador_biblioteca
      self.__tela = TelaUsuario(self)
      self.__usuarios = []

  def abre_tela(self):
    [opcao] = self.__tela.tela_opcoes()

     if opcao == 1:
      self.incluir_usuario(nome: str, email: str, id_usuario: str)
    elif opcao == 2:
      self.excluir_usuario(id_usuario: str)
    elif opcao == 3:
      self.listar_usuarios()

    # essa função serve para instanciar um objeto usuario e colocar na lista de usuarios
  def incluir_usuario(self, nome: str, email: str, id_usuario: str):
    self.__usuarios.append(Usuario(nome,email,id_usuario))

    # essa funçao percorre toda a lista de usuário para localizar o registro com o id_usuario que foi passado como parametro. quando acha esse registro, o objeto é removido
  def excluir_usuario(self, id_usuario: str):
    if isinstance (id_usuario, str):
      for usuario in self.__usuarios:
        if usuario.id_usuario = id_usuario:
          self.__usuarios.remove(usuario) 

  #essa funcao retorna a lista de usuarios
  def listar_usuarios(self):
    lista_usuarios = []
    for usuario in self.__usuarios:
      lista_usuarios.append(usuario.nome)
      #invocação do método próprio da tela para exibição da lista ao invés do print. O método recebe uma lista de strings. Ela incia vazia e a cada iteração é adicionado o usuario.nome
    self.__tela.exibir_lista(lista_usuarios)

  # percorrer a lista e retornar o objeto do usuario cujo parametro id_usuario seja igual ao parametro id_usuario da funcao de listagem
  def listar_usuario_por_id(self, id_usuario: str):
    if isinstance(id_usuario, str):
      for usuario in self.__usuarios:
        if usuario.id_usuario == id_usuario
          return usuario