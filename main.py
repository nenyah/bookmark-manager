from bs4 import BeautifulSoup
import json

path = r'./bookmarks_2019_4_8.html'


def parse_bookmark(path):
    result = []
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'lxml')
        a = soup.select('a')

        for el in a:
            result.append(el.attrs)
    return result


result = parse_bookmark(path)
print(result[0]['href'])
