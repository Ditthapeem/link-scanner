from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def get_links(url: str):
    url_list = []

    # Split link out of tag
    for tag in url:
        link = tag.split('"')[1]

        # Delete fragment or query
        fragment_query = False
        true_link = ""
        for i in link:
            if i == "#" or i == "?":
                fragment_query = True
            if not fragment_query:
                true_link += i

        if true_link not in url_list and len(true_link) != 0:
            url_list.append(true_link)

    return url_list


url = ['<a href="https://kucafe.com/menu">',
       '<a href="https://kucafe.com/menu#breakfast">',
       '<a href="https://kucafe.com/search?q=coffee">',
       '<a href="#prices">']
print(get_links(url))
