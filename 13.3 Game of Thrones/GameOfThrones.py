import urllib2
import BeautifulSoup as BS
import re

if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/Game_of_Thrones"
    urlwiki = "https://en.wikipedia.org"
    page = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(page)

    adaptation_link = soup.find("li", attrs={"class": "toclevel-2 tocsection-10"}).a["href"]
    adaptation_url = url + adaptation_link
    adaptation_page = urllib2.urlopen(adaptation_url).read()
    adaptation_soup = BS.BeautifulSoup(adaptation_page)

    season1_link = adaptation_soup.find("table", attrs={"class": "wikitable"}).a["href"]
    season1_url = urlwiki + season1_link
    season1_page = urllib2.urlopen(season1_url).read()
    season1_soup = BS.BeautifulSoup(season1_page)

    table1 = season1_soup.find("table", attrs={"class": "wikitable plainrowheaders wikiepisodetable"})
    if table1:
        episode_view1 = table1.find("tr", attrs={"class": "vevent"})
        if episode_view1:
            almost1 = episode_view1.findAll("td")[-1].text
            #views1 = float(re.sub("\[?[0-9]+\]", "", almost1))

    season2_link = adaptation_soup.find("a", attrs={"title": "Game of Thrones (season 2)"})["href"]
    season2_url = urlwiki + season2_link
    season2_page = urllib2.urlopen(season2_url).read()
    season2_soup = BS.BeautifulSoup(season2_page)

    season3_link = adaptation_soup.find("a", attrs={"title": "Game of Thrones (season 3)"})["href"]
    season3_url = urlwiki + season3_link
    season3_page = urllib2.urlopen(season3_url).read()
    season3_soup = BS.BeautifulSoup(season3_page)

    season4_link = adaptation_soup.find("a", attrs={"title": "Game of Thrones (season 4)"})["href"]
    season4_url = urlwiki + season4_link
    season4_page = urllib2.urlopen(season4_url).read()
    season4_soup = BS.BeautifulSoup(season4_page)

    season5_link = adaptation_soup.find("a", attrs={"title": "Game of Thrones (season 5)"})["href"]
    season5_url = urlwiki + season5_link
    season5_page = urllib2.urlopen(season5_url).read()
    season5_soup = BS.BeautifulSoup(season5_page)

    season6_link = adaptation_soup.find("a", attrs={"title": "Game of Thrones (season 6)"})["href"]
    season6_url = urlwiki + season6_link
    season6_page = urllib2.urlopen(season6_url).read()
    season6_soup = BS.BeautifulSoup(season6_page)

    season7_link = adaptation_soup.find("a", attrs={"title": "Game of Thrones (season 7)"})["href"]
    season7_url = urlwiki + season7_link
    season7_page = urllib2.urlopen(season7_url).read()
    season7_soup = BS.BeautifulSoup(season7_page)
