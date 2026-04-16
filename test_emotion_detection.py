import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=input_json, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}")

    data = json.loads(response.text)
    emotions = data['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion

    items = [f"'{k}': {v}" for k, v in emotions.items() if k != "dominant_emotion"]
    formatted_items = ", ".join(items)

    return f"For the given statement, the system response is {formatted_items}. The dominant emotion is \033[1m{emotions['dominant_emotion']}."
