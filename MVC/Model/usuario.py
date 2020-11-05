class Usuario:

    def __init__(self, nome: str, email: str, id_usuario: str):
        if isinstance((nome, str) and (email, str)):
            self.__nome = nome
            self.__email = email
            self.__id_usuario = id_usuario
            self.__aquisicoes = []

        @property
        def nome(self):
            return self.__nome

        @nome.setter
        def nome(self, novo_nome):
                self.__nome = novo_nome

        @property
        def email(self):
            return self.__email

        @email.setter
        def email(self, novo_email):
            self.__email = novo_email

        @property
        def id_usuario(self):
            return id_usuario

        @id_usuario.setter
        def id_usuario(self, novo_id):
            self.__id_usuario = novo_id


        @property
        def aquisicoes(self):
            return self.__aquisicoes