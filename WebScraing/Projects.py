import requests
from bs4 import BeautifulSoup

File_Path = 'movie_list.txt'
response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best'
                        '-movies-2/')

website_data = response.text
soup = BeautifulSoup(website_data, 'html.parser')

# Getting Name of title of all films
TitleofAllFilms = [value.getText() for value in soup.find_all(name="h3", class_='title')]

with open(File_Path, 'w') as file:
    for movie in TitleofAllFilms[::-1]:
        try:
            file.write(f"{movie}\n")
        except:
            print("All Data inserted")
