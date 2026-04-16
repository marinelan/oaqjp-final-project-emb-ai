import requests
import json

def emotion_detector(text_to_analyze):
    # API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers  
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Payload/input
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Send POST request to the API
    response = requests.post(url, json=input_json, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}")
    else:
        return response.text