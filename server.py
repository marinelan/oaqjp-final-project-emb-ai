from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)
@app.route('/emotionDetector')
def emotion_detect():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    items = [f"'{k}': {v}" for k, v in response.items() if k != "dominant_emotion"]
    formatted_items = ", ".join(items)

    return f"For the given statement, the system response is {formatted_items}. The dominant emotion is {response['dominant_emotion']}."


@app.route("/") 
def render_index_page(): 
    return render_template('index.html')

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000)