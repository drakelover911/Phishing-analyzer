from main import final_function, connection_1, data, sql
with open("columns.txt", "r") as f:
    columns = f.read().splitlines()
c, conn = sql(columns)
driver = connection_1()
for element in data:
    try:
        driver.get(element)
        result = final_function(element, driver)
        keys = ", ".join([f'"{k}"' for k in result.keys()])
        placeholders = ", ".join(["?"] * len(result))
        values = list(result.values())
        sql = f'INSERT INTO results (url, {keys}) VALUES (?, {placeholders})'
        c.execute(sql, [element] + values)
    except Exception as e:
        print("Error:", e)
conn.commit()
conn.close()
driver.quit()
