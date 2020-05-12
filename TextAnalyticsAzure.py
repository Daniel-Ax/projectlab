#A project tematikája az hogy a Microsoft Azure Cognitive Service API-ja segítségével elemzem ki hogy egy szöveg hangulata milyen.
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import API_ELEMENTS

def authenticate_client():
    ta_credential = AzureKeyCredential(API_ELEMENTS.key)
    text_analytics_client = TextAnalyticsClient(endpoint=API_ELEMENTS.endpoint, credential=ta_credential)
    return text_analytics_client


def sentiment_analysis(client):
    documents = ["I had the best day of my life. I wish you were there with me."]
    response = client.analyze_sentiment(documents=documents)[0]
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    ))
    for idx, sentence in enumerate(response.sentences):
        print("[Length: {}]".format(sentence.grapheme_length))
        print("Sentence {} sentiment: {}".format(idx + 1, sentence.sentiment))
        print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
            sentence.confidence_scores.positive,
            sentence.confidence_scores.neutral,
            sentence.confidence_scores.negative,
        ))


def language_detection(client):
    try:
        documents = ["저는 Miklós Horthy의 군인입니다"]
        response = client.detect_language(documents = documents, country_hint = 'us')[0]
        print("Language: ", response.primary_language.name)

    except Exception as err:
        print("Encountered exception. {}".format(err))


if __name__ == "__main__":
    client = authenticate_client()
    language_detection(client)
    sentiment_analysis(client)
