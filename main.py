from fetch_reviews import get_review
from sentiment_prediction import get_sentiment_overview

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://www.amazon.com/Cycling-Gloves-Mountain-Bike-Shock-Absorbing/product-reviews/B08VS7L5WG/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
    get_review(url)

    get_sentiment_overview()