from ExtratorArgumentosUrl import ExtratorArgumentosUrl


url = input('Entre com a url: ')

if (ExtratorArgumentosUrl.url_valida(url)):
    extrator = ExtratorArgumentosUrl(url)
    extrator1 = ExtratorArgumentosUrl(url)

    print(extrator1 == extrator)

    url_base = extrator.extrai_url_base()
    print(f'url base: {url_base}')

    modulo = extrator.extrai_modulo()
    print(f'modulo: {modulo}')

    argumentos = extrator.extrai_argumentos()
    print(f'argumentos: {argumentos}')
else:
    print("A URL não é válida.")