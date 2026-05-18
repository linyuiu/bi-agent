import duckdb

duck_db = duckdb.connect("query.db")\

duck_db.execute("""CREATE TABLE orders AS SELECT * FROM read_csv_auto('data/orders.csv')""")

