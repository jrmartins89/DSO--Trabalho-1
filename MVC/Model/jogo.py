class Jogo:
    def __init__(self, genero: str, nome: str, ano_lancamento: int, horas_jogadas: int, preco: float,
                 total_trofeus: int, finalizado: bool, multiplayer: bool):
        if isinstance(nome, str):
            self.__genero = genero
            self.__nome = nome
            self.__ano_lancamento = ano_lancamento
            self.__horas_jogadas = horas_jogadas
            self.__preco = preco
            self.__total_trofeus = total_trofeus
            self.__finalizado = finalizado
            self.__multiplayer = multiplayer
            self.__jogos = []

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, novo_genero):
        self.__genero = novo_genero

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def ano_lancamento(self):
        return self.__ano_lancamento

    @ano_lancamento.setter
    def ano_lancamento(self, novo_ano_lancamento):
        self.__ano_lancamento = novo_ano_lancamento

    @property
    def horas_jogadas(self):
        return self.__horas_jogadas

    @horas_jogadas.setter
    def horas_jogadas(self, novas_horas_jogadas: int):
        self.__horas_jogadas = novas_horas_jogadas

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco

    @property
    def total_trofeus(self):
        return self.__total_trofeus

    @total_trofeus.setter
    def total_trofeus(self, novo_total_trofeus):
        self.__total_trofeus = novo_total_trofeus

    @property
    def finalizado(self):
        return self.__finalizado

    @finalizado.setter
    def finalizado(self, novo_finalizado):
        self.__finalizado = novo_finalizado

    @property
    def multiplayer(self):
        return self.__multiplayer

    @multiplayer.setter
    def multiplayer(self, novo_multiplayer):
        self.__multiplayer = novo_multiplayer

    @property
    def jogos(self):
     return self.__jogos

