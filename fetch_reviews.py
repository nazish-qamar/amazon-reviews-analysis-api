import requests
from bs4 import BeautifulSoup


# Follow the instruction in 'finding_header_data.md' file to get the header
HEADERS = ({'authority': 'www.amazon.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # Requests sorts cookies= alphabetically
            # 'cookie': '',
            'device-memory': '8',
            'downlink': '1.1',
            'dpr': '1',
            'ect': '4g',
            'rtt': '150',
            'sec-ch-device-memory': '8',
            'sec-ch-dpr': '1',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-viewport-width': '1920',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'viewport-width': '1920', })


def getdata(url):
    r = requests.get(url, headers=HEADERS)
    return r.text


def html_code(url):
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
    return (soup)


def customer_review(url):

    if url.split("/")[3] != "-":    ## This is for amazon.com
        url_review = url.split("/")[0] + "/" + \
                 url.split("/")[1] + "/" + \
                 url.split("/")[2] + "/" + \
                 url.split("/")[3] + "/" + \
                 "product-reviews/" + \
                 url.split("/")[5] + "/" + "ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=1"

    else:                     ### for parsing amazon.de
        url_review = url.split("/")[0] + "/" + \
                     url.split("/")[1] + "/" + \
                     url.split("/")[2] + "/" + \
                     url.split("/")[3] + "/" + \
                     url.split("/")[4] + "/" + \
                     url.split("/")[5] + "/" + \
                     "product-reviews/" + \
                     url.split("/")[
                         7] + "/" + "ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=1"

    data_str = ""
    total_pages_scraped = 0
    while True:
        if total_pages_scraped > 10:
            break

        soup = html_code(url_review)
        all_reviews = soup.find_all("span", class_="a-size-base review-text review-text-content")

        pageExisted = False
        for item in all_reviews:
            pageExisted = True
            data_str = data_str + item.get_text()

        #next_page = soup.find_all("li", class_="a-disabled a-last")
        if not pageExisted:
            break

        temp_url = url_review.split("=")
        now = str(int(temp_url[-1]) + 1)
        temp_url[-1] = now
        url_review = ("=".join(temp_url))
        total_pages_scraped += 1

    result = data_str.split("\n")

    rev_result = []
    for i in result:
        if i == "":
            pass
        else:
            rev_result.append(i)

    return rev_result


def get_review(url):
    product_review = {}
    item_review = customer_review(url)
    product_review["title"] = str(" ".join((url.split("/")[3]).split("-")))
    product_review["comments"] = str([str(row) for row in item_review if row != ""])
    product_review["url"] = url
    return product_review