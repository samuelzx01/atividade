

#criação do banco e conexao

import mysql.connector as my

def connectar_banco():
    connect = my.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'loja'
    )
    return connect
    return connect

# 1. Cadastrar novo produto 

def cadastrar_produto(produto, preco):
    connect = connectar_banco()
    cursor = connectar_banco.cursor()
    sql = f'insert into loja_produtos(produto,preco) values ("{produto}, {preco}")'
    cursor.execute(sql)
    connect.commit()
    connect.close()

# 2. Listar todos os produtos 

def listar_produto():
    connect = connectar_banco()
    cursor = connectar_banco.cursor()
    sql = 'select * from loja_produtos'
    cursor.execute(sql)
    connect.commit()
    connect.close()



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




