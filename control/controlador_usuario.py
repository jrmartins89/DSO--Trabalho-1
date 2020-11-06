from MVC.model.usuario import Usuario
from MVC.view.tela_usuario import TelaUsuario

class ControladorUsuario:
  def __init__(self, controlador_biblioteca):
      self.__controlador_biblioteca = controlador_biblioteca
      self.__tela = TelaUsuario(self)
      self.__usuarios = []

  def abre_tela(self):
    #evocaco do método do menu criado na classe de tela 
    #[opcao, nome, email, id_usuario] = self.__tela.tela_opcoes()
      [opcao, usuario] = self.__tela.tela_opcoes()
    
      if opcao == 1:
        self.incluir_usuario(usuario)
      elif opcao == 2:
        self.excluir_usuario(usuario)
      elif opcao == 3: 
        self.listar_usuarios()

    # essa função serve para instanciar um objeto usuario e colocar na lista de usuarios
    #def incluir_usuario(self, nome: str, email: str, id_usuario: str):#
  def incluir_usuario(self, usuario: Usuario ):
    print("entrou na funcao")
    #for usuario in self.__usuarios:
    if usuario not in self.__usuarios:
      self.__usuarios.append(usuario)
    print("Usuário adicionado com sucesso!") #adicionado conferencia se usuario ja existe para que não seja adicionado duplicado. E mensagem de confirmação de adição de usuário a lista. Mas ainda não funcionando. - André

    # essa funçao percorre toda a lista de usuário para localizar o registro com o id_usuario que foi passado como parametro. quando acha esse registro, o objeto é removido
  def excluir_usuario(self, id_usuario: str):
    print("entrou na funcao")
    for usuarios in self.__usuarios: 
      if usuarios.id_usuario == id_usuario:
        self.__usuarios.remove(usuarios) 
        print("O usuário foi excluído.") # ainda não funcionando.

  #essa funcao retorna a lista de usuarios
  def listar_usuarios(self):
    lista_usuarios = []
    for usuarios in self.__usuarios:
      lista_usuarios.append(usuarios.nome)
      #invocação do método próprio da tela para exibição da lista ao invés do print. O método recebe uma lista de strings. Ela incia vazia e a cada iteração é adicionado o usuario.nome
    print("listando usuarios...")
    self.__tela.mostra_lista_str(lista_usuarios)

  # percorrer a lista e retornar o objeto do usuario cujo parametro id_usuario seja igual ao parametro id_usuario da funcao de listagem
  def listar_usuario_por_id(self, id_usuario: str):
    if isinstance(id_usuario, str):
      for usuario in self.__usuarios:
        if usuario.id_usuario == id_usuario:
          return usuario