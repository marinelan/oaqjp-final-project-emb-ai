"Application activation module"

# Import the libraries
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the server file
app = Flask(__name__)

# Route the app
@app.route('/emotionDetector')

def emotion_detect():
    "Returns the response to the client's input"
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    items = [f"'{k}': {v}" for k, v in response.items() if k != "dominant_emotion"]
    formatted_items = ", ".join(items)
    return (
        f"For the given statement, the system response is {formatted_items}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    "Renders the template"
    return render_template('index.html')

# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
