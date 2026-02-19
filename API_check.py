from pysafebrowsing import SafeBrowsing
import os
from dotenv import load_dotenv
load_dotenv()

KEY = os.getenv("GOOGLE_API_KEY")
s = SafeBrowsing(KEY)
def is_url_valid(url):
    if ((url.startswith("https://") or url.startswith("http://")) and " " not in url and "." in url):
        return True
    else:
        return False
    
def check_API(url):
    r = s.lookup_urls([url])
    url_data = r[url]
    return url_data['malicious']

url = input("Enter URL link: ")
url_valid= is_url_valid(url)
if not url_valid:
    print("Is this URL valid:", url_valid)
else:
    print("URL is valid. Making API request")
    print("Is this link malicious:",check_API(url))