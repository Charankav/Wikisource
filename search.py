import requests
from bs4 import BeautifulSoup

search_url = "https://ml.wikipedia.org/w/index.php?go=പോകൂ&search=കത&title=പ്രത്യേകം%3Aഅന്വേഷണം&ns0=1"

# Send a GET request to the search URL
response = requests.get(search_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the elements that contain article titles
    title_elements = soup.find_all('div', class_='mw-search-result-heading')

    # Extract and print the article titles
    for title_element in title_elements:
        article_title = title_element.text.strip()
        print(article_title)
else:
    print(f"Failed to retrieve search results. Status code: {response.status_code}")
