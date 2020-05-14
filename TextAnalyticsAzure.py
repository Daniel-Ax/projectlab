#A project tematikája az hogy a Microsoft Azure Cognitive Service API-ja segítségével elemzem ki hogy egy szöveg hangulata milyen.
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import API_ELEMENTS



#documents = ["I had the best day of my life. I wish you were there with me."]
documents=["에서 파티를 취소했다고요. 제가 이제 여기 이제 왕자가 형이라고 얘기를 할 겸 워낙 친해서 문자를 나누다가 너무 잘 하고 있으니까 제가 아휴 시간도 안 먹고 이러고 있는데 베이커가 나온다고 있기 때문에 오늘이 크리스마스거든요. 25일 맞아요."]
def authenticate_client():
    ta_credential = AzureKeyCredential(API_ELEMENTS.key)
    text_analytics_client = TextAnalyticsClient(endpoint=API_ELEMENTS.endpoint, credential=ta_credential)
    return text_analytics_client


def sentiment_analysis(client):

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
        response = client.detect_language(documents = documents, country_hint = 'us')[0]
        print("Language: ", response.primary_language.name)

    except Exception as err:
        print("Encountered exception. {}".format(err))


if __name__ == "__main__":
    client = authenticate_client()
    language_detection(client)
    sentiment_analysis(client)
