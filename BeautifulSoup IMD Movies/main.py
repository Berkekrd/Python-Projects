import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://www.google.com"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

movie_name = []
year = []
time = []
rating = []

movie_data = soup.findAll('div', attrs={'class': 'ipc-metadata-list-summary-item__c'})
for store in movie_data:
    name = store.find('h3').text
    metadata_items = store.find_all('span', class_='sc-b189961a-8 kLaxqf dli-title-metadata-item')
    
    if len(metadata_items) == 3:
        year_of_release = metadata_items[0].text
        runtime = metadata_items[1].text
        movie_rating = metadata_items[2].text

        movie_name.append(name)
        year.append(year_of_release)
        time.append(runtime)
        rating.append(movie_rating)

        print(f"Name: {name}, Year of Release: {year_of_release}, Runtime: {runtime}, Rating: {movie_rating}")

# Create a DataFrame
data = {
    'Name': movie_name,
    'Year': year,
    'Runtime': time,
    'Rating': rating
}
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('movies.csv', index=False)

print("CSV file has been created successfully.")
