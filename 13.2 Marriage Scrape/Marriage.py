import urllib2
import BeautifulSoup as BS

if __name__ == '__main__':
    url = "http://quotes.yourdictionary.com/theme/marriage/"
    page = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(page)
    quotes = soup.findAll("p", attrs={"class": "quoteContent"})
    #authors = soup.findAll("a", attrs={"class": "author_link_tag"})

    for quote in quotes:
        print quote.string
