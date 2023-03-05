# amazon-reviews-sentiment
#### A streamlit based API for scraping customer review for an amazon product and predict the sentiment classification overview of the reviews

### Demo: https://nazish-qamar-amazon-reviews-analysis-api-main-ux0gr4.streamlit.app/
### Technical details:
#### 1) Streamlit library for interactive dashboard
#### 2) fetch_reviews.py : web scraping implementation using beautiful soup library
#### 3) database_utility.py: logic for storing and retrieving scraped reviews in SQLite database file
#### 4) sentiment_prediction.py: sentiment prediction of the stored reviews using Transformer model. Currently using the HuggingFace model (Ref: https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment


### Instructions:
#### 1) Run the main.py file using command "streamlit run main.py"
#### 2) Click the API URL or copy from the terminal and paste it in the browser to open the API interface
#### 3) Choose the options from the drop-down menu, i.e., Option 1: retrieve already stored reviews; Option 2: Fetch review for new product.
#### 4a) For Option 1, select the product from the drop-down menu, and click predict button.
#### 4b) For Option 2, copy the URL from the product page and paste it in input field and press enter
