import psycopg


DB_CONFIG = {
    "dbname":"bi_agent",
    "user":"root",
    "password":"South@2025@23",
    "host":"wisonic.top",
    "port":"65432",
}






# def execute_pgsql(sql):
#     CURSOR = conn.cursor()
#
#     CURSOR.execute(f"""{sql}""")
#     rows = CURSOR.fetchall()
#
#     CURSOR.close()
#     conn.close()
#
#     return rows

def execute_pgsql(sql: str):
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()

