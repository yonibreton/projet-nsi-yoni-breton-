import sqlite3
def database_connexion(db_file):
    connexion = None
    connexion = sqlite3.connect(db_file)

    return connexion
conn = database_connexion("data/imdb.db")

def execute_sql(connexion,sql):
    cur = connexion.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

run_sql = execute_sql
sql = " SELECT COUNT(primaryTitle) FROM title_basics;"
run_sql(conn,sql)