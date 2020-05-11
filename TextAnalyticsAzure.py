#A project tematikája az hogy a Microsoft Azure Cognitive Service API-ja segítségével elemzem ki hogy egy szöveg hangulata milyen.
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import API_ELEMENTS

def authenticate_client():
    ta_credential = AzureKeyCredential(API_ELEMENTS.key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=API_ELEMENTS.endpoint, credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

print(client)