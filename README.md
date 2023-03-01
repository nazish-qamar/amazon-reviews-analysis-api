# amazon-reviews-sentiment
 A streamlit based API for scraping customer review for an amazon product and predict the sentiment classification report

### Demo: https://nazish-qamar-amazon-reviews-analysis-api-main-ux0gr4.streamlit.app/
### Technical details:
#### 1) Streamlit library for interative dashboard
#### 2) fetch_reviews.py : web scraping implementation using beautiful soup library
#### 3) database_utility.py: logic for storing and retrieving scraped reviews in SQLite database file
#### 4) sentiment_prediction.py: sentiment predict stored reviews using transformer model.

### Instructions:
#### 1) Run the main.py file using command "streamlit run main.py"
#### 2) Click the API URL
#### 3) Choose the options from the drop-down menu, i.e., Option 1: Fetch review for new product; Option 2: retrieve already stored reviews.
#### 4a) For Option 1, copy the URL from the product page and paste it in input field and press enter
#### 4b) For Option 2, select the product from the drop-down menu, and click predict button.
