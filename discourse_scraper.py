import requests
from bs4 import BeautifulSoup

def scrape_discourse(base_url, start_page=1, end_page=2):
    all_links = []
    for page in range(start_page, end_page + 1):
        url = f"{base_url}?page={page}"
        response = requests.get(url)
        if response.status_code != 200:
            continue
        soup = BeautifulSoup(response.text, 'html.parser')
        topics = soup.find_all("a", class_="title raw-link raw-topic-link")
        for topic in topics:
            link = topic.get("href")
            if link:
                all_links.append("https://discourse.onlinedegree.iitm.ac.in" + link)
    
    for link in all_links:
        print(link)

if __name__ == "__main__":
    scrape_discourse("https://discourse.onlinedegree.iitm.ac.in/c/programming/tds/71", start_page=1, end_page=3)
