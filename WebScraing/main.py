from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
website_data = response.text
soup = BeautifulSoup(website_data, 'html.parser')
collect = [value.getText() for value in soup.find_all(name='span', class_="titleline")]
linkAddress = [value.get('href') for value in soup.select('span a', class_='titleline')]
upvote = [int(value.getText().split()[0]) for value in soup.find_all(name='span', class_='score')]
print(collect)
print(f"Length of Title {len(collect)}")
print(linkAddress)
print(f"Length of Link Address {len(linkAddress)}")
print(upvote)
print(f"Length of upvote {len(upvote)}")
print(upvote.index(max(upvote)))