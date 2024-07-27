def arquivoExiste(nome):
    try:
        file = open(nome, 'rt')
        file.close()
        
    except FileNotFoundError:
        return False
    
    else:
        return True
    
    
def criarArquivo(nome):
    try:
        file = open(nome, 'wt+')
        file.close()
        
    except:
        print('Houve um erro na criação do arquivo!')
        
    else:
        print(f'Arquivo {nome} criado com sucesso!')
        
        
def lerArquivo(nome):
    try:
        file = open(nome, 'rt')
        
    except:
        print('Erro ao ler o arquivo!')
        
    else:
        from funcoes import mostrarLinhas  # Importação local
        mostrarLinhas()
        print(file.read())
    finally:
        file.close()
        
        
def cadastrar(arq, comboDesejado):
    try:
        file = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        file.write(f'{comboDesejado}\n')
        print(f'Pedido do combo {comboDesejado} cadastrado com sucesso!')
        file.close()