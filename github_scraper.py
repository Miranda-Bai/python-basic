import argparse
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By

# cdp = "D:\Developer\chromedriver.exe"
# s = webdriver.ChromeService(executable_path=cdp)
# driver = webdriver.Chrome(service=s)

def get_all_repos(url):
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
        joined_url = base_url + "/" + repo
       
        tempLst.append(joined_url)

    return tempLst

def get_file_page(repo):
    driver.get(repo)
    res = driver.find_elements(By.CLASS_NAME, "react-directory-truncate")
    for file in res:
        file = file.find_element(By.TAG_NAME, "a")
        filename = file.text

        if "py" in filename:
            fileurl = f"{repo}/blob/main/{filename}"
            return going_for_raw(fileurl)

def going_for_raw(fileurl):
    driver.get(fileurl)
    # types__StyledButton-sc-ws60qy-0 
    raw = driver.find_element(By.CLASS_NAME, "dTgfec")
    raw.click()
    file_content = driver.page_source
    return f"{file_content}"


def main():
    parser = argparse.ArgumentParser(description="Scraping HTML")
    parser.add_argument("--url", required=True, help="URL to scrape.")
    parser.add_argument("--keyword", required=False, help="The keyword needs to find in the URL page.")
    
    args = parser.parse_args()

    url = args.url + "?tab=repositories"
    
    global driver
    
    driver = webdriver.Chrome()
    repoLst = get_all_repos(url)

    if repoLst is not None and len(repoLst) != 0:
        repoLst = join_repo_url(args.url, repoLst)
        print(repoLst)

        for repo in repoLst:
            file_content = get_file_page(repo)
            if file_content is not None and file_content != "" and args.keyword is not None and args.keyword != "":
                if args.keyword in file_content:
                    print(f"Find {args.keyword}!")
                    print(file_content.find(args.keyword))

    driver.quit()
    
if __name__ == "__main__":
    main()
    



    