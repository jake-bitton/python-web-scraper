from bs4 import BeautifulSoup
import requests
import io

'''
REMEMBER TO ACTIVATE VENV (workon webScraper) before working on this.
'''

def Scrape(urls: str | list[str], tag: str='a', get_val: str='href'):
    
    assert urls.isinstance(list[str] | str)

    f = None
    try:
        f = open("site_data.txt", "a")
    except Exception as e:
        print(f'An exception occurred when opening the file: {e}')
    finally:
        if f is not None:
            f.close()

    #   Converts str url into a 1 elem list if necessary and then scrapes each item in the list of urls.
    if urls.isinstance(str):
        url = [urls]
            
    for l in url | urls:
        response = requests.get(l)
        f.write(f'Now writing from {l}:')
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            # Extract all of desired HTML tag
            tags = soup.find_all(tag)
            for t in tags:
                f.write(f'\t{t}\n')

        else:
            f.write(f'\tError: {response.status_code} in URL: {l}\n')
    
    f.close()