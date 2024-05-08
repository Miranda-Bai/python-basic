import argparse
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By

# cdp = "D:\Developer\chromedriver.exe"
# s = webdriver.ChromeService(executable_path=cdp)
# driver = webdriver.Chrome(service=s)

def get_all_repos(driver, url):
    repoLst = []
    driver.get(url)
    res = driver.find_elements(By.CLASS_NAME, "wb-break-all")
    for tag in res:
        tag = tag.find_element(By.TAG_NAME, "a")
        # print(tag.text)
        repoLst.append(tag.text)

    return repoLst

def join_repo_url(base_url, repoLst):
    tempLst = []
    for repo in repoLst:
        tempLst.append(urljoin(base_url, repo))

    return tempLst

def main():
    parser = argparse.ArgumentParser(description="Scraping HTML")
    parser.add_argument("--url", required=True, help="URL to scrape.")
    parser.add_argument("--keyword", required=False, help="The keyword needs to find in the URL page.")
    
    args = parser.parse_args()

    url = args.url + "?tab=repositories"
    

    driver = webdriver.Chrome()
    repoLst = get_all_repos(driver, url)

    if repoLst is not None and len(repoLst) != 0:
        repoLst = join_repo_url(args.url, repoLst)

    

    driver.quit()
    
if __name__ == "__main__":
    main()
    



    