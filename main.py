from URL_stats import features
from dynamic_stats import features1, connection, connection_1, whois_connect
import pandas as pd

with open("spam.txt", "r") as f:
        keywords = f.read()

dd = pd.read_csv("top500Domains.csv", usecols=["Root Domain"])
popular_domains = set(dd["Root Domain"])

driver = connection_1()
def final_function(url, driver):
        response, score = connection(url)
        w = whois_connect(url)
        f_dynamic = features1(url, response, driver, w, score, keywords) 
        f_url = features(url, popular_domains)
    
        final = f_dynamic | f_url
        return final

with open ("list.txt", "r") as f:
    data = f.read().splitlines()
driver.get(data[0])
results_for_sql = final_function(data[0], driver)
columns = list(results_for_sql.keys())
driver.quit()
        