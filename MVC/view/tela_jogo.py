from tela import Tela


class TelaJogo(Tela):
    def __init__(self, controlador_jogo):
        self.controlador_jogo = controlador_jogo

    # esse método recebe uma lista como parametro, percorre ela e exibe os elementos da mesma
    def exibir_menu_opcoes(self, lista: []):
        for elem in lista:
            print(elemen)

    # # tratar quando o usuário não digitar nem 1,2,3 e opção 0 para voltar para o menu principal
    def tela_opcoes(self):
        print("Bem vindo à Biblioteca Gamer!")
        print("Escolha uma opção do menu abaixo:")
        print("1: Adicionar Jogo")
        print("2: Remover Jogo")
        print("3: Listar Jogos")
        opcao = int(input("Opção"))
        # as variáveis iniciam vazias e só recebem valores se as opcoes selecionadas forem 1 ou 2
        # horas_jogadas poderia começar com 0  e finalizado com false, o que acha? - André
        # E acho que isso é definido na classe jogo mesmo, não na tela - André
        # nome = None
        # genero = None
        # ano_lancamento = None
        # horas_jogadas = None
        # preco = None
        # total_trofeus = None
        # finalizado = None
        # multiplayer = None
        if (opcao == 1):
            # Muita coisa que o usuário precisaria digitar só para remover o jogo, melhor um outro if para isso
            nome = input("Nome do jogo: ")
            genero = input("Gênero do jogo:")
            ano_lancamento = int(input("Ano de lancamento do jogo:"))
            horas_jogadas = int(input("Horas jogadas:"))
            preco = float(input("Preço do jogo:"))
            finalizado = bool(input(
                "O jogo já foi finalizado? Digite s se sim e n se não."))  # necessário método para converter "s" em True e "n" em False
            multiplayer = bool(input(
                "O jogo é multiplayer? Digite s se sim e n se não"))  # necessário método para converter "s" em True e "n" em False
            total_trofeus = int(input("Qual o total de trofeus no jogo:"))

            return [opcao, nome, genero, ano_lancamento, horas_jogadas, preco]

            if (opcao == 2):
                nome = input("Digite o nome do jogo que deseja excluir : ")
            return [opcao, nome]

            # esse return esta devolvendo pro método abre_tela do contorlador do jogo. O controlador do usuario chama a tela e realiza o processo de leitura e impressao e retorna os valores. O controlador pega esses valores de retorno para realizar as operacoes
