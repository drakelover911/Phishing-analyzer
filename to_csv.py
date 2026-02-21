import sqlite3
import pandas as pd

conn = sqlite3.connect("data.db")

df = pd.read_sql_query("SELECT * FROM results", conn)

print(df.head())
df.to_csv("results.csv", index=False)