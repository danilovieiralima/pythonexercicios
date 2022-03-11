def escreva(texto):
    tamanho = len(texto) + 4
    print('=' * tamanho)
    print(f'  {texto}')
    print('=' * tamanho)


mensagem = str(input('Digite algo: ')).strip()
escreva(mensagem)
