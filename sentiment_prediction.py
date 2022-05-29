import csv
from transformers import pipeline

def load_review():
    reviews = []
    with open("Cycling-Gloves-Mountain-Bike-Shock-Absorbing.csv", "r") as fp:
        csv_reader = csv.reader(fp, delimiter="\n")
        for row in csv_reader:
            row_whole = " ".join(row)
            reviews.append(row_whole)
    return reviews

def get_sentiment_overview():
    #https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment
    #sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    sentiment_pipeline = pipeline("sentiment-analysis")

    reviews = load_review()
    senti = sentiment_pipeline(reviews)
    pos = 0
    neg = 0
    for each in senti:
        if each['label'].lower()   == "positive":
            pos +=1
        elif each['label'].lower()   == "negative":
            neg +=1

    positive_percentage = "Positivity rate: " + str(round(100 * pos/(neg + pos),2)) + " %"
    print(positive_percentage)