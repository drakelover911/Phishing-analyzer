from URL_stats import features
from dynamic_stats import features1, connection, connection_1, whois_connect
import pandas as pd
import sqlite3


def sql(columns):
    conn = sqlite3.connect("data1.db")
    c = conn.cursor()
    columns_sql = ", ".join([f'"{col}" TEXT' for col in columns])
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

with open("spam.txt", "r") as f:
        keywords = f.read()
with open("test.txt", "r") as d:
       data = d.read().splitlines()
dd = pd.read_csv("top500Domains.csv", usecols=["Root Domain"])
popular_domains = set(dd["Root Domain"])

driver = connection_1()
def final_function(url, driver):
        response, score = connection(url)
        w = whois_connect(url)
        f_dynamic = features1(url, response, driver, w, score, keywords) 
        f_url = features(url, popular_domains)
    
        final = f_url | f_dynamic
        return final 

