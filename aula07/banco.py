import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name  # Opcional, pode ser especificado depois
        )
        print("Conexão com o MySQL bem-sucedida!")
    except Error as e:
        print(f"O erro '{e}' ocorreu")
    return connection

def execute_query(connection, query, params=None):
    cursor = connection.cursor()
    try:
        cursor.execute(query, params or ()) # Usar tupla vazia se params for None
        connection.commit() # Necessário para INSERT, UPDATE, DELETE
        print("Query executada com sucesso")
    except Error as e:
        print(f"O erro '{e}' ocorreu ao executar a query")

def execute_read_query(connection, query, params=None):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query, params or ())
        result = cursor.fetchall() # Pega todos os resultados
        return result
    except Error as e:
        print(f"O erro '{e}' ocorreu ao executar a query de leitura")
    return result

# --- Exemplo de uso ---
if __name__ == '__main__':
    # Substitua com suas credenciais e nome do banco de dados
    meu_banco = "senaidb" # O nome que você usou no USE
    conn = create_connection("localhost", "root", "senai", meu_banco)

    if conn is not None and conn.is_connected():
        # Exemplo de INSERT (usando placeholders para segurança)
        insert_vendedor_query = "INSERT INTO Vendedores (Nome) VALUES (%s)"
        execute_query(conn, insert_vendedor_query, ("João Silva",))
        execute_query(conn, insert_vendedor_query, ("Maria Oliveira",))

        # Exemplo de SELECT
        select_vendedores_query = "SELECT IDVendedor, Nome FROM Vendedores"
        vendedores = execute_read_query(conn, select_vendedores_query)

        if vendedores:
            print("\nVendedores cadastrados:")
            for vendedor in vendedores:
                print(vendedor)

        # Exemplo de INSERT na tabela Vendas com data formatada
        # Lembre-se que a coluna 'Data' no MySQL espera 'YYYY-MM-DD'
        # Se você tem a data como string no Python, pode formatá-la antes ou usar STR_TO_DATE no SQL
        data_venda_str = "01/01/2016" # Formato DD/MM/YYYY
        # Convertendo para YYYY-MM-DD para o Python ou usando STR_TO_DATE no SQL
        # Opção 1: Converter no Python (se a data já estiver no formato YYYY-MM-DD, não precisa)
        # from datetime import datetime
        # data_obj = datetime.strptime(data_venda_str, '%d/%m/%Y')
        # data_mysql_format = data_obj.strftime('%Y-%m-%d')
        # insert_venda_query = """
        # INSERT INTO Vendas (IDVendedor, IDCliente, Data, Total)
        # VALUES (%s, %s, %s, %s)
        # """
        # execute_query(conn, insert_venda_query, (1, 1, data_mysql_format, 8053.60))

        # Opção 2: Usar STR_TO_DATE diretamente no SQL (como você fez no Workbench)
        insert_venda_query_com_str_to_date = """
        INSERT INTO Vendas (IDVendedor, IDCliente, Data, Total)
        VALUES (%s, %s, STR_TO_DATE(%s, '%d/%m/%Y'), %s)
        """
        execute_query(conn, insert_venda_query_com_str_to_date, (1, 1, data_venda_str, 8053.60))


        # Fechar a conexão
        if conn.is_connected():
            conn.close()
            print("Conexão com o MySQL fechada.")
    else:
        print("Não foi possível conectar ao banco de dados.")