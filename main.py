## gereciamento de pedidos usando funções
from funcoes import opcao, mostrarLinhas, arq
from arquivo.file_pag import arquivoExiste, criarArquivo, lerArquivo

def main():
    if not arquivoExiste(arq):
        criarArquivo(arq)

    mostrarLinhas()
    nome = input('Digite o seu nome: ')
    mostrarLinhas()
    lerArquivo(arq)
    print(f'Olá, {nome}! Iremos começar o seu atendimento.')
    mostrarLinhas()

    opcao()

    lerArquivo('pedidos.txt')

if __name__ == "__main__":
    main()