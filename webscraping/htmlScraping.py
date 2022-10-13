import bs4
import requests

# to bring the full data to basic page
bring = requests.get('https://www.english-exam.org/IELTS/')

# print(bring.text)
# to identify part of the page
part_of_page = bs4.BeautifulSoup(bring.text ,'html.parser') # => to know the page   ,, to takle the data by html


my_part = part_of_page.select('#main > div > p:nth-child(2)')   #=> copy this by copy selector
# print(my_part)

# to get the text only 
print(my_part[0].getText())