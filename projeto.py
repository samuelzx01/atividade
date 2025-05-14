

#criação do banco e conexao

import mysql.connector as my

def connectar_banco():
    connect = my.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'loja'
    )
    return connect

# 1. Cadastrar novo produto 

def cadastrar_produto(produto, preco):
    connect = connectar_banco()
    cursor = connect.cursor()
    sql = f'insert into loja_produtos(produto,preco) values ("{produto}", "{preco}")'
    cursor.execute(sql)
    connect.commit()
    connect.close()

# 2. Listar todos os produtos 





# 3. Atualizar produto 





# 4. Remover produto 


def remover_produto(id_produto):
    
    connect = connectar_banco()
    cursor = connectar_banco.cursor()
    sql = f"delete from loja_produtos where id = '{id_produto}'"
    cursor.execute(sql)
    connect.commit()
    connect.close()





# 5. Sair 

# 8. Sair 


while True:
    opcoes = input('1 - cadastrar\n2 - listar\n3 - atualizar\n4 - remover\n5 - Sair')
    if (opcoes == '5'):
        print('Saindo...')
        break
    if (opcoes == '1'):
         produto = input('digite o nme do produto:  ')
         preco = input('digite o valor do produto:  ')
         cadastrar_produto(produto, preco)
         print('prduto adicionado com sucesso...')
        

    if (opcoes == 2):
        produtos = listar_produtos()

        for produto in produtos:
            print(f'ID:{produto['id_produto']}')

    
        
        

    
         


