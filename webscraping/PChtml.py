from importlib.resources import path
import bs4
from pathlib import Path
path_file = open(Path.home() / Path('D:','another.html'))
scr = bs4.BeautifulSoup(path_file ,'html.parser')
elements = scr.select('body > table > tbody > tr:nth-child(4) > td:nth-child(1)')
# elements = scr.select('body')
print(elements)
print(elements[0].getText())

