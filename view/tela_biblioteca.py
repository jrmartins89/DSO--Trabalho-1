class TelaBiblioteca:
  def __init__ (self,controlador_biblioteca):
    self.controlador_biblioteca = controlador_biblioteca
    
  #esta é a primeira tela que o usuário vê quando o sistema iniciar
  def tela_opcoes(self):
    print("Bem vindo à Biblioteca Gamer!")
    print("Selecione a opção desejada:")
    print("1: Menu de usuários")
    print("2: Menu de Jogos")
    print("3: Menu de Aquisições")
    opcao = int(input("Opção"))
    
    return [opcao, nome, genero, ano_lancamento, horas_jogadas, preco]
  #esse return esta devolvendo pro método abre_tela do contorlador do jogo. O controlador do usuario chama a tela e realiza o processo de leitura e impressao e retorna os valores. O controlador pega esses valores de retorno para realizar as operacoes
    