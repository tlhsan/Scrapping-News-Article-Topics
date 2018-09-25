import requests
from newspaper import Article
from bs4 import BeautifulSoup
import csv

# creating a csv file
csv_file = open('articles_sample5.csv', 'w', newline='')
field_name = ['article_topics']
writer = csv.DictWriter(csv_file, fieldnames=field_name)
writer.writeheader()

bag = set()

articles = ['first']
duplicate_checker = ''

def create_csv(art_string):
    #for i in range(1,len(articles)):
    writer.writerow({'article_topics':art_string})




def get_link(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    bs = BeautifulSoup(plain_text,'lxml')
    for link in bs.findAll('a'):
        href = link.get('href')
        article_links = checkLink(href)
        try:


            if 'https://www.thedailystar.net/frontpage' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/business/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/business' == article_links:
                get_links_2(article_links)
            if 'https://www.thedailystar.net/country/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/country' == article_links:
                get_links_2(article_links)

            if 'https://www.thedailystar.net/opinion/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/opinion' == article_links:
                get_links_2(article_links)

            if 'https://www.thedailystar.net/sports/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/sports' == article_links:
                get_links_2(article_links)
            if 'https://www.thedailystar.net/arts-entertainment/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/arts-entertainment' == article_links:
                get_links_2(article_links)
            if 'https://www.thedailystar.net/lifestyle/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/lifestyle' == article_links:
                get_links_2(article_links)
            if 'https://www.thedailystar.net/bytes/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/bytes' == article_links:
                get_links_2(article_links)
            if 'https://www.thedailystar.net/showbiz/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/showbiz' == article_links:
                get_links_2(article_links)
            if 'https://www.thedailystar.net/shout/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/shout' == article_links:
                get_links_2(article_links)
            if 'https://www.thedailystar.net/star-weekend/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/star-weekend' == article_links:
                get_links_2(article_links)
            if 'https://www.thedailystar.net/star-youth/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/star-youth' == article_links:
                get_links_2(article_links)
            else:
                continue
        except:
            pass


def get_link_items(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    global duplicate_checker
    global articles
    global bag
    bs = BeautifulSoup(plain_text, 'lxml')
    try:
        for link in bs.findAll('h1', {'itemprop':'headline'}):

            art_string = link.string

            #create_csv(art_string)
            # if art_string in duplicate_checker:
            #     continue
            # else:
            #     #create_csv(art_string)
            #     print(art_string)
            #     duplicate_checker = art_string

            if art_string not in bag:
                print(art_string)

                articles +=[art_string]
                bag.add(art_string)
                create_csv(art_string)
            else:
                continue

            #writer.writerow({'article_topics':art_string})
            #print(link.string)
            #print(articles[link.string])
            #write_file('linksList.txt', link.string)
    except:
        pass
def get_links_2(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    bs = BeautifulSoup(plain_text, 'lxml')
    for link in bs.findAll('a'):
        #print('from url2-------------------------------------------------------')
        href = link.get('href')
        article_links = checkLink(href)
        try:
            if 'https://www.thedailystar.net/business/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/country/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/opinion/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/sports/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/arts-entertainment/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/lifestyle/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/bytes/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/showbiz/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/shout/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/star-weekend/' in article_links:
                get_link_items(article_links)
            if 'https://www.thedailystar.net/star-youth/' in article_links:
                get_link_items(article_links)
            else:
                continue
        except:
            pass



def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def checkLink(url):
    try:
        link = ''
        if "https://www.thedailystar.net" in url:
            link = url
        else:
            link = "https://www.thedailystar.net" + url
    except:
        exit()

    return link





get_link('https://www.thedailystar.net')
#print(articles)
#print(articles)
#get_link_items('https://www.thedailystar.net/frontpage/the-greatest-show-begins-1591378')
#print(articles)
#create_csv(articles)


