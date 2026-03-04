from main import final_function, data, sql
from dynamic_stats import connection_1
import time
from concurrent.futures import ThreadPoolExecutor
import queue as q
import numpy as np
import threading

chunks = np.array_split(data, 7)
with open("columns.txt", "r") as f:
    columns = f.read().splitlines()
#to robi kazdy watek
queue = q.Queue()
def worker(url_chunk):
    count = 0
    driver = connection_1()
    for element in url_chunk:
        time.sleep(1.5)
        if count == 75:
            driver.quit()
            count = 0
            try:
                driver = connection_1()
            except Exception as s:
                print(s)
                raise
        try:
            driver.get(element)
        except Exception as s:
            print(s) 
            try:
                driver.quit()
            except:
                pass
            try: 
                driver = connection_1()
            except:
                print("Restart failed")
                break
            continue
        try:
            result = final_function(element, driver)
            queue.put((element, result))
        except Exception as e:
            print("Error:", e)
        count +=1
    driver.quit()


# to robi jeden
def writer():
    c, conn = sql(columns)
    while True:
        item = queue.get()
        if item is None:
            break
        element, result = item
        keys = ", ".join([f'"{k}"' for k in result.keys()])
        placeholders = ", ".join(["?"] * len(result))
        values = list(result.values())
        sql_ = f'INSERT INTO results (url, {keys}) VALUES (?, {placeholders})'
        c.execute(sql_, [element] + values)
        queue.task_done()
    conn.commit()
    conn.close()

writer_thread = threading.Thread(target=writer)
writer_thread.start()

with ThreadPoolExecutor(max_workers=7) as executor:
    executor.map(worker, chunks)

queue.put(None)
writer_thread.join()
