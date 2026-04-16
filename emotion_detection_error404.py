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
    
    # 400 error handling
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
    }
   
    # Convert raw JSON string into dictionary
    data = json.loads(response.text)
    
    # Extract the emotions and their scores from the response
    emotions = data['emotionPredictions'][0]['emotion']
    
    # Dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Add the dominant emotion to the emotions dictionary
    emotions['dominant_emotion'] = dominant_emotion
    
    return emotions
