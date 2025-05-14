opcoes = input('1 - cadastrar\n2 - listar\n3 - atualizar\n4 - remover\n5 - Sair')
while True:
    if (opcoes == '5'):
        print('Saindo...')
        break
    if (opcoes == '1'):
         produto = input('digite o nme do produto')
         preco = input('digite o valor do produto')
         print('produto inserido com sucesso')

    if (opcoes == 2):
        produtos = listar_produtos()

        for produto in produtos:
            print(f'ID:{produto['id_produto']}')

    if(opcoes == 3):
        ...

    
         




#criação do banco e conexao



# 1. Cadastrar novo produto 






# 2. Listar todos os produtos 





# 3. Atualizar produto 





# 4. Remover produto 






# 5. Sair 