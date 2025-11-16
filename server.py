from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetection")
def emotion_detector():

    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    emotion_list = ['emotionPredictions'][0]['emotion']

    # 1. Storing Anger's Score

    anger_score = emotion_list['anger']

    highest_score = anger_score

    dominant_emotion = 'anger'

    # 2. Storing and Evaluating Disgust's Score

    disgust_score = emotion_list['disgust']

    if disgust_score > highest_score:
        highest_score = disgust_score
        dominant_emotion = 'disgust'
    
    # 3. Storing and Evaluating Fear's Score
    
    fear_score = emotion_list['fear']

    if fear_score > highest_score:
        highest_score = fear_score
        dominant_emotion = 'fear'
    
    # 4. Storing and Evaluating Joy's Score

    joy_score = emotion_list['joy']

    if joy_score > highest_score:
        highest_score = joy_score
        dominant_emotion = 'joy'
    
    # 5. Storing and Evaluating Sadness's Score

    sadness_score = emotion_list['sadness']

    if sadness_score > highest_score:
        highest_score = sadness_score
        dominant_emotion = 'sadness'

    # Returning the final text

    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(anger_score, disgust_score, fear_socre, joy_score, sadness_score, dominant_emotion)


@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)