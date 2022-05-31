from fetch_reviews import get_review
from sentiment_prediction import get_sentiment_overview

if __name__ == '__main__':
    url = "https://www.amazon.com/Aiw-Wfdnn-Beanie-Trust-DeepHeather/dp/B07HY25PQ6/ref=sr_1_2?keywords=gaming%2Bhats&pd_rd_r=a37e132e-358f-4645-84d4-f0e8532384d4&pd_rd_w=bIa6V&pd_rd_wg=rHpMJ&pf_rd_p=09483392-9ac6-434a-a3d7-39d83662f54a&pf_rd_r=X6PC9DZEVSHW1XB0Y12J&qid=1653944503&sr=8-2&th=1&psc=1"
    url_review = url.split("/")[0] + "/" + \
                 url.split("/")[1] + "/" + \
                 url.split("/")[2] + "/" + \
                 url.split("/")[3] + "/" + \
                 "product-reviews/" + \
                 url.split("/")[5] + "/" + "ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
    get_review(url_review)

    get_sentiment_overview()