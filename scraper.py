from bs4 import BeautifulSoup
import requests
import io



def Scrape(url: str, tag: str='a', get_val: str='href'):
    f = None
    try:
        f = open("site_data.txt", "a")
    except Exception as e:
        print(f'An exception occurred when opening the file: {e}')
    finally:
        if f is not None:
            f.close()
            
    #  Target URL

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract all of desired HTML tag
        tags = soup.find_all(tag)
        for t in tags:
            f.write(f'{t}\n')
        f.close()
    else:
        print(f'Error: {response.status_code}')
        f.close()