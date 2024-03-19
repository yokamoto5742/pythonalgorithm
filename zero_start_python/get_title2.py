from bs4 import BeautifulSoup

with open('ranking.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print(soup.title.string)
