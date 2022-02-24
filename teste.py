
import psycopg2 as db
import pandas as pd


#Trazendo as tabelas categoria e funcionario
conn = db.connect( 
    host="#####",
    user="#####",
    dbname="#####",
    password="######")
categoria= pd.read_sql_query("SELECT * FROM public.categoria",conn)
funcionario= pd.read_sql_query("SELECT * FROM public.funcionario",conn)
#Normalizando as tabelas
categoria.rename(columns={'id':'id_categoria'},inplace=True)
funcionario.rename(columns={'id':'id_funcionario'},inplace=True)

#Conectando a Instancia_C e trazendo o maior id de venda
conn = db.connect( 
    host="#####",
    user="#####",
    dbname="#####",
    password="######")
ultima_venda_C = pd.read_sql_query("SELECT * FROM vendas_funcionario WHERE id_venda = ( SELECT MAX (id_venda) FROM vendas_funcionario);",conn)

#Conectando na instancia_A e trazendo as novas vendas, com 'id_venda' maior do que os que estão registrados
conn = db.connect( 
    host="#####",
    user="#####",
    dbname="#####",
    password="######")
vendas = pd.read_sql_query((f"SELECT *FROM public.venda WHERE id_venda > {int(ultima_venda_C['id_venda'])}"),conn)
vendas = vendas.merge(categoria,how='left',on='id_categoria')
vendas = vendas.merge(funcionario,how='left',on='id_funcionario')
vendas = vendas.loc[:,['id_venda','data_venda','venda','nome_funcionario','nome_categoria']]

#Conectando na Instancia_C para gravar os novos registros
conn = db.connect( 
    host="#####",
    user="#####",
    dbname="#####",
    password="######")
cursor_C = conn.cursor()

for index, row in vendas.iterrows():
    cursor_C.execute("INSERT INTO public.vendas_funcionario(id_venda, data_venda, venda, nome_funcionario, nome_categoria) VALUES(%s,%s,%s,%s,%s)",(row.id_venda, row.data_venda, row.venda,row.nome_funcionario,row.nome_categoria))
conn.commit()
cursor_C.close()

print(vendas)


