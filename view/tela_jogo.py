from MVC.view.tela import Tela


class TelaJogo(Tela):
    def __init__(self, controlador_jogo):
        self.controlador_jogo = controlador_jogo

    # esse método recebe uma lista como parametro, percorre ela e exibe os elementos da mesma
    def mostra_lista_str(self, lista: []):
        for elem in lista:
            print(elem)

    
    def tela_opcoes(self):
      print("Bem vindo à Biblioteca Gamer!")
      print("Escolha uma opção do menu abaixo:")
      print("1: Adicionar Jogo")
      print("2: Remover Jogo")
      print("3: Listar Jogos")
      opcao = int(input("Opção: "))
        
      if opcao == 1:
        nome = input("Nome do jogo: ")
        genero = input("Gênero do jogo:")
        ano_lancamento = int(input("Ano de lancamento do jogo:"))
        horas_jogadas = int(input("Horas jogadas:"))
        total_trofeus = int(input("Qual o total de trofeus no jogo:"))
        return [opcao, nome, genero, ano_lancamento, horas_jogadas, total_trofeus]

      elif opcao == 2:
        nome = input("Digite o nome do jogo que deseja excluir: ")
        genero = None
        ano_lancamento = None
        horas_jogadas = None
        total_trofeus = None
        return [opcao, nome, genero, ano_lancamento, horas_jogadas,  total_trofeus]
        
      elif opcao ==3:
        opcao = None
        nome = None
        genero = None
        ano_lancamento = None
        horas_jogadas = None 
        total_trofeus = None
        return [opcao, nome, genero, ano_lancamento,horas_jogadas,total_trofeus]
            # esse return esta devolvendo pro método abre_tela do contorlador do jogo. O controlador do usuario chama a tela e realiza o processo de leitura e impressao e retorna os valores. O controlador pega esses valores de retorno para realizar as operacoes