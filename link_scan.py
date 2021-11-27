from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from urllib.error import HTTPError
import urllib.request
import ssl
import sys
from typing import List


def get_links(url):
    url_list = []

    # Delete fragment or query
    for link in url:
        fragment_query = False
        true_link = ""
        if link != None:
            for i in link:
                if i == "#" or i == "?":
                    fragment_query = True
                if not fragment_query:
                    true_link += i
        if true_link not in url_list and len(true_link) != 0:
            url_list.append(true_link)
    return url_list



def is_valid_url(url: str):
    context = ssl._create_unverified_context()
    my_request = urllib.request.Request(url, method="HEAD")
    try:
        response = urllib.request.urlopen(my_request, context=context)
        return True
    except HTTPError as e:
        if e.code == 403:
            return True
        return False

def invalid_urls(urllist: List[str]) -> List[str]:
    invalid_url_list = []
    for i in urllist:
        if is_valid_url(i) == False:
            invalid_url_list.append(i)
    return invalid_url_list


if __name__ == '__main__':
    url_list = []
    # Set Firefox
    my_options = Options()
    my_options.add_argument("--headless")
    browser = webdriver.Firefox(options=my_options)
    browser.get(sys.argv[1])
    link_list = browser.find_elements_by_tag_name("a")
    # Set url
    for i in link_list:
        if i.tag_name == 'a':
            url_list.append(i.get_attribute('href'))
    list = get_links(url_list)
    for i in list:
        print(i)
    print()
    print("Bad Links:")
    bad_link = invalid_urls(list)
    for i in bad_link:
        print(i)

