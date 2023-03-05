import csv
import ast
from transformers import pipeline
import tensorflow_text as text
import tensorflow as tf


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
    #For using pretranied BERT model from Huggingface, uncomment the code below
    #sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    #sentiment_pipeline = pipeline("sentiment-analysis")
    #senti = sentiment_pipeline(result)

    dataset_name = 'imdb'
    saved_model_path = './{}_bert'.format(dataset_name.replace('/', '_'))
    reloaded_model = tf.saved_model.load(saved_model_path)
    reloaded_results = tf.sigmoid(reloaded_model(tf.constant(result)))
    pos = 0
    neg = 0
    for i in range(len(result)):
        if reloaded_results[i][0] > 0.5:
            pos += 1
        else:
            neg += 1

    show_result ={}
    show_result["total_reviews"]= (pos+neg)
    show_result["positive"] = pos

    return (show_result)