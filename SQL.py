from main import final_function, connection_1
import sqlite3

def sql(columns):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    columns_sql = ", ".join([f'"{col} FLOAT"' for col in columns])
    sql_ = f"""
    CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    {columns_sql}
    )
    """
    c.execute(sql_)
    conn.commit()
    return c, conn
