from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import argparse

def get_page(url):
    try:
        response = requests.get(url)
    except:
        print(f"Get {url} failed!")
        return
    
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

def spider_urls(url, keyword, visited_urls):
    urls = []

    page = get_page(url)
    
    if page is None or page == "":
        return
    
    # print(type(page))
    tags = page.find_all('a')
    for tag in tags:
        href = tag.get("href")
        if href is not None and href != "":
            urls.append(href)
    

    for link in urls:
        if link not in visited_urls:
            visited_urls.append(link)
            # print("link: ", link)
            url_join = urljoin(url, link)
            if keyword in url_join:
                print(url_join)
                spider_urls(url_join, keyword, visited_urls)

def main():
    parser = argparse.ArgumentParser(description="Scraping HTML")
    parser.add_argument("--url", required=True, help="URL to scrape.")
    parser.add_argument("--keyword", required=True, help="The keyword needs to find in the URL page.")
    
    args = parser.parse_args()

    visited_urls = []

    spider_urls(args.url, args.keyword, visited_urls)
   
    # # find the first <a> tag
    # link = page.find("a")

    # # print the innertext of the found <a> tag
    # print(link.string)

   
# https://en.wikipedia.org/wiki/Programmer

if __name__ == "__main__":
    main()