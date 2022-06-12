# amazon-reviews-analysis-api
The project aims at scraping the customer reviews from a product on amazon website and predict the percentage of positive reviews.
The api is an interactive streamlit based dashboard that provides user options to scrape a new product review or to predict the sentiment overview of the product reviews.

##Files Information
###main.py
####The starting point of the project that provides an interface for different modules.

###fetch_reviews.py
####Contains the logic for fetching the user reviews by giving the product URL as an input.

###sentiment_prediction.py
####Contains the logic for sentiment prediction of review available for a product chosen from the drop-down menu.

###database_utility.py
####A SQLite database utility file that provides APIs for storing and loading the user reviews for a product.

###requirements.txt
####The file contains the list of all the required libraries
