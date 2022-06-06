from fetch_reviews import get_review
from sentiment_prediction import get_sentiment_overview
from database_utility import ReviewDatabase
import streamlit as st

if __name__ == '__main__':
    db_object = ReviewDatabase("product_reviews")
    db_object.create_table()

    st.title("Product Reviews Overview")
    choice = st.selectbox("Select Action", ("Scrape Reviews", "Predict Sentiment"))

    if "Scrape Reviews" == choice:
        st.write("Please copy the complete URL of the product page and paste below!")
        url = st.text_input("Product URL")
        if url:
            reviews_dict = get_review(url)
            db_object.add_data(reviews_dict)
            st.write("Done!")

    else:
        files = db_object.get_product_titles()
        file_choice = st.selectbox("Choose the review file for sentiment overview", files)
        content = db_object.get_product_review(file_choice)

        st.write("Product URL:", content[2])

        button_choice = st.button('Predict Review Sentiment!')
        if button_choice:
            with st.spinner('Wait for it...'):
                review_msg = get_sentiment_overview(content[1])
                st.write("Total Reviews: " + str(review_msg["total_reviews"]))
                st.write("Positive Reviews: " + str(review_msg["positive"]))
