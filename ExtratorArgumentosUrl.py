class ExtratorArgumentosUrl:

    def __init__(self, url: str):
        self.__url = url

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, valor: str):
        if valor:
            self.__url = valor
        else:
            raise ValueError("A Url não pode ser vazia.")

    @staticmethod
    def url_valida(url: str) -> bool:
        if url:
            return True
        else:
            return False

    def extrai_url_base(self) -> str:
        indexBarra = self.__url.find('/', 8)
        url_base = self.__url[:indexBarra]
        return url_base

    def extrai_modulo(self) -> str:
        modulo: str = ''
        indexBarra: int = self.__url.find('/', 8)
        indexInterrogacao: int = self.__url.find('?')
        if(indexInterrogacao >= 0):
            modulo = self.__url[indexBarra: indexInterrogacao]
        else:
            modulo = self.__url[indexBarra: ]
        return modulo


    def extrai_argumentos(self) -> dict:
        argumentos: dict = {}
        url_quebrada: list = self.__url.split('?')
        if(len(url_quebrada) > 1):
            for termo in url_quebrada[1].split('&'):
                pairs = termo.split('=')
                argumentos[pairs[0]] = pairs[1]

        return argumentos

    def __str__(self):
        if (self.__url is None):
            url_base = self.extrai_url_base()
            modulo = self.extrai_modulo()
            argumentos = self.extrai_argumentos()
            return f'url_base: {url_base}\n' \
                   f'modulo: {modulo}\n' \
                   f'argumentos: {argumentos}'
        else:
            return ''

    def __eq__(self, other):
        if (isinstance(other, ExtratorArgumentosUrl)):
            return self.__url == other.__url
        else:
            return False