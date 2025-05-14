#  Opa

import mysql as my

def conectar_banco():
    connect = my.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'loja',

    )


