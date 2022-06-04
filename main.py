from fetch_reviews import get_review, get_available_files
from sentiment_prediction import get_sentiment_overview
import streamlit as st

if __name__ == '__main__':
    st.title("Amazon Reviews Sentiment")
    choice = st.selectbox("Select Action", ("Scrape Reviews", "Predict Sentiment"))

    if "Scrape Reviews" == choice:
        st.write("Please copy the complete URL of the product page and paste below!")
        url = st.text_input("Product URL")
        if url:
            get_review(url)
            st.write("Done!")

    else:
        files = get_available_files()
        file_choice = st.selectbox("Choose the review file for sentiment overview", files)

        button_choice = st.button('Predict Review Sentiment!')
        if button_choice:
            with st.spinner('Wait for it...'):
                positive_percentage = get_sentiment_overview(file_choice)
                st.write(positive_percentage)