# Import 'Flask', 'render_template', and 'request' from 'flask'
from flask import Flask, render_template, request
# Import 'emotion_detector' function from 'emotion_detection'
from EmotionDetection.emotion_detection import emotion_detector

# Name the application
app = Flask("Emotion Detector")

# Set the route for the javascript page
@app.route("/emotionDetector")
# Define the function
def emotion_function():

    # Analyzing the Text
    text_to_analyze = request.args.get("textToAnalyze")

    # Storing the Analyzed Result
    response = emotion_detector(text_to_analyze)

    # If the value of the key 'dominant_emotion' is equal to 'None', then...
    if response['dominant_emotion'] is None:
        # Terminamte the function by returning a default string
        return "Invalid text! Please try again!"

    # 1. Storing Anger's Score
    anger_score = response['anger']
    highest_score = anger_score
    dominant_emotion = 'anger'
    # 2. Storing and Evaluating Disgust's Score
    disgust_score = response['disgust']
    if disgust_score > highest_score:
        highest_score = disgust_score
        dominant_emotion = 'disgust'
    # 3. Storing and Evaluating Fear's Score
    fear_score = response['fear']
    if fear_score > highest_score:
        highest_score = fear_score
        dominant_emotion = 'fear'
    # 4. Storing and Evaluating Joy's Score
    joy_score = response['joy']
    if joy_score > highest_score:
        highest_score = joy_score
        dominant_emotion = 'joy'
    # 5. Storing and Evaluating Sadness's Score
    sadness_score = response['sadness']
    if sadness_score > highest_score:
        highest_score = sadness_score
        dominant_emotion = 'sadness'
    # Returning the final text
    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(anger_score, disgust_score, fear_score, joy_score, sadness_score, dominant_emotion)

#Set the route of the app
@app.route("/")
def render_index_page(): # Define the rendering
    # Render the interface on the 'index.html' page
    return render_template("index.html")

if __name__ == "__main__": # If this script is the main file, then...
    # Run the app
    app.run(host="0.0.0.0", port=5000)
