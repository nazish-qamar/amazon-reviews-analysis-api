import csv
import ast
from transformers import pipeline

def load_review(review_choice):
    reviews = []
    with open(review_choice, "r") as fp:
        csv_reader = csv.reader(fp, delimiter="\n")
        for row in csv_reader:
            row_whole = " ".join(row)
            reviews.append(row_whole)
    return reviews

def get_sentiment_overview(content):
    result = ast.literal_eval(content)
    #sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    sentiment_pipeline = pipeline("sentiment-analysis")
    senti = sentiment_pipeline(result)
    pos = 0
    neg = 0
    for each in senti:
        if each['label'].lower() == "positive":
            pos += 1
        elif each['label'].lower() == "negative":
            neg += 1

    show_result ={}
    show_result["total_reviews"]= (pos+neg)
    show_result["positive"] = pos
    return (show_result)