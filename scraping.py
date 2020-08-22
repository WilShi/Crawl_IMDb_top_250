import re
import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Create all required lists
ranks=[]
movie_names=[]
links=[]
Rating_Values=[]
Directors=[]
Writers=[]
Stars=[]
casts=[]
Genres=[]
Certificate=[]
Country=[]
Language=[]
Release_Date=[]
Filming_Locations=[]
Budget=[]
Opening_Weekend_USA=[]
Gross_USA=[]
Cumulative_Worldwide_Gross=[]
Runtime=[]

def make_soup(url):
    """
    Use requests and BeautifulSoup 4 library to turn the parameter 
    URL into and return HTML code in BeautifulSoup format.
    """
    html = requests.get(url) #Creat html file by url
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html5lib')
    return soup

def get_movie(soup):
    """
    Return dictionary of rank, movie name and movie information link.
    """
    rank = 1;
    movies = {}
    link = 'https://www.imdb.com'
    if soup.find_all('td', class_='titleColumn') != []:
        for tdtag in soup.find_all('td', class_='titleColumn'):
            info = {}
            year = tdtag.find_all('span', class_='secondaryInfo')[0].text
            info[tdtag.find_all('a')[0].text + ' ' + year] = link + tdtag.find_all('a')[0].get('href')
            movies[str(rank)] = info
            rank += 1
    return movies

def blok(name, soup, type_list):
    """
    Set information from class 'txt-block' to corresponding list 
    """
    for date in soup.find_all('div', class_='txt-block'):
        if name in date.text:
            date = date.text.lstrip()
            date = ' '.join(date.split())
            if (':' in date):
                type_list.append(date[date.find(':')+2:])
            else:
                type_list.append(date)
            print(date)
            return 0

def info(url):
    """
    Set all detail information from movie's information page to corresponding list 
    """
    soup = make_soup(url)
    if soup.find_all('span', itemprop="ratingValue"):
        for ratingValue in soup.find_all('span', itemprop="ratingValue"):
            print('Rating Value:', ratingValue.text)
            Rating_Values.append(ratingValue.text)
    else:
        Rating_Values.append('')

    if soup.find_all('div', class_='credit_summary_item'):
        d=0
        w=0
        s=0
        for summary in soup.find_all('div', class_='credit_summary_item'):
            title = summary.find_all('h4')[0].text
            names = []
            for name in summary.find_all('a'):
                name = re.sub(r'<[^>]*>', '', str(name)).lstrip()
                names.append(name)
            names = ', '.join(names)
            if 'Director' in title:
                Directors.append(names)
                d=1
            if 'Writers' in title:
                Writers.append(names)
                w=1
            if 'Stars' in title:
                Stars.append(names)
                s=1
            print(title, names)
        if d == 0:
            Directors.append('')
        if w == 0:
            Writers.append('')
        if s == 0:
            Stars.append('')
    else:
        Directors.append('')
        Writers.append('')
        Stars.append('')
        
    if soup.find_all('div', class_='article', id='titleCast'):
        c_list = []
        for article in soup.find_all('div', class_='article', id='titleCast'):
            for cast_list in article.find_all('table', class_='cast_list'):
                for cast in cast_list.find_all('tr', class_='odd'):
                    for name in cast.find_all('td', class_=''):
                        name = name.text.lstrip()
                        name = ' '.join(name.split())
                        c_list.append(name)
        c_list = ', '.join(c_list)
        casts.append(c_list)
        print("cast_list", c_list)
    else:
        casts.append('')

    if soup.find_all('div', class_='see-more inline canwrap'):
        for keywords in soup.find_all('div', class_='see-more inline canwrap'):
            title = keywords.find_all('h4', class_='inline')[0].text
            words = []
            if title == 'Genres:':
                for c_type in keywords.find_all('a'):
                    c_type = re.sub(r'<[^>]*>', '', str(c_type)).lstrip()
                    words.append(c_type)
                Genres.append(c_type)
                print(title, c_type)
    else:
        Genres.append('')

    
    blok('Country', soup, Country)
    blok('Language', soup, Language)
    blok('Release Date', soup, Release_Date)
    blok('Filming Locations', soup, Filming_Locations)
    blok('Budget', soup, Budget)
    blok('Opening Weekend USA', soup, Opening_Weekend_USA)
    blok('Gross USA', soup, Gross_USA)
    blok('Cumulative Worldwide Gross', soup, Cumulative_Worldwide_Gross)
    blok('Runtime', soup, Runtime)
    blok('Certificate', soup, Certificate)

    for i in ranks, links, Rating_Values, Directors, Writers, Stars, casts, Genres, \
        Certificate, Country, Language, Release_Date, Filming_Locations, Budget, \
            Opening_Weekend_USA, Gross_USA, Cumulative_Worldwide_Gross, Runtime:
        if len(i) != len(Directors):
            i.append('')
    print('\n')

def movies_info(movies_dict):
    """
    Use link of movie's information page call info function to crawl information, 
    and set all information to corresponding list 
    """
    for key in movies_dict:
        rank = key
        for name in movies_dict[key]:
            movie_name = name
            link = movies_dict[key][name]

        ranks.append(rank)
        movie_names.append(movie_name)
        links.append(link)

        print(rank, movie_name, link)
        info(link)

if __name__ == '__main__':
    url = "https://www.imdb.com/chart/top/"
    soup = make_soup(url)
    movies = get_movie(soup)
    movies_info(movies)
    
    num=1 # Check the size of all lists
    for i in ranks, links, Rating_Values, Directors, Writers, Stars, casts, \
        Genres, Certificate, Country, Language, Release_Date, Filming_Locations, \
            Budget, Opening_Weekend_USA, Gross_USA, Cumulative_Worldwide_Gross, Runtime:
        print(num, len(i))
        num += 1

    # Integrate all lists into pandas format (dataframe)
    dataframe = pd.DataFrame({'Rank': ranks, 'Movie Names': movie_names, 
    'Links': links, 'Rating Values': Rating_Values, 'Directors': Directors, 
    'Writers': Writers, 'Stars': Stars, 'Casts': casts, 'Genres': Genres, 
    'Certificate': Certificate, 'Country': Country, 'Language': Language, 
    'Release Date': Release_Date, 'Filming Locations': Filming_Locations, 
    'Budget': Budget, 'Opening Weekend USA': Opening_Weekend_USA, 
    'Gross USA': Gross_USA, 'Cumulative Worldwide Gross': Cumulative_Worldwide_Gross, 'Runtime': Runtime})

    # Make the organized dataframe into a CSV file named IMDb_top_250.csv and save it in the current directory
    dataframe.to_csv("IMDb_top_250.csv",index=False,sep=',') 