from MVC.view.tela import Tela


class TelaUsuario(Tela):
    def __init__(self, controlador_usuario):
        self.controlador_usuario = controlador_usuario

    # esse método recebe uma lista como parametro, percorre ela e exibe os elementos da mesma
    def exibir_menu_opcoes(self, lista: []):
        for elem in lista:
            print(elem)

    def tela_opcoes(self):
        print("Bem vindo à Biblioteca Gamer!")
        print("Escolha uma opção do menu abaixo:")
        print("1: Adicionar usuário")
        print("2: Remover usuário")
        print("3: Listar usuários")
        opcao = int(input("opção:"))
        # # tratar quando o usuário não digitar nem 1,2,3 e opção 0 para voltar para o menu principal
        # a variável inicia vazia e só recebe um valor de fato se as opcoes selecionadas forem 1 ou 2
        # e o método listar usuário por ID? falta incluir ali - André
        #nome = None
        if opcao == 1:
            nome = input("Qual o nome do usuario:")
            email = input("Qual o email do usuario:")
            id_usuario = input("Qual o id do usuário:")
            return [opcao, nome, email, id_usuario]
    #       print("Usuário adicionado com sucesso!") 
        elif opcao == 2:
            nome = None
            email = None
            id_usuario = input("Digite o id do usuário que deseja remover: ")
            return [opcao, nome, email, id_usuario]
        elif opcao == 3:
            nome = None
            email = None
            id_usuario = None
            return [opcao, nome, email, id_usuario]
 # esse return esta devolvendo pro método abre_tela do contorlador do usuario. O controlador do usuario chama a tela e realiza o processo de leitura e impressao e retorna os valores. O controlador pega esses valores de retorno para realizar alguma operacao