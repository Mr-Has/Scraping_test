from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
# using prettify to  make the printed result more readable
# print(soup.prettify())

# To grab information from html (easily we access it as an atrebute)
# Just getting the title
# match = soup.title.text
# print(match)

# Extracing between the <div>
# match = soup.div
# print(match)

# If we use the .find() method, we can pass argument to narrow down what we are looking for.
# These arguments can match any attrebute that the tag may have.
# We use class_= key word.
# match = soup.find('div', class_='footer')
# print(match)

# To parss html and get all the articles and summery
for article in soup.find_all('div', class_='article'):

    #  To dig down into the text of the headline
    #  We use the article instead of the full html, we have it from line 24
    # <h2><a>
    headline = article.h2.a.text
    print(headline)

    # Also summery
    summery = article.p.text
    print(summery)

    print()