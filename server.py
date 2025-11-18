"""
This is the server
"""

# Import 'Flask', 'render_template', and 'request' from 'flask'
from flask import Flask, render_template, request
# Import 'emotion_detector' function from 'emotion_detection'
from EmotionDetection.emotion_detection import emotion_detector

# Name the application
app = Flask("Emotion Detector")


@app.route("/emotionDetector") # Set the route for the javascript page


def emotion_function():
    '''
    Define the emotion function
    '''

    # Analyzing the Text
    text_to_analyze = request.args.get("textToAnalyze")

    # Storing the Analyzed Result
    response = emotion_detector(text_to_analyze)

    # If the value of the key 'dominant_emotion' is equal to 'None', then...
    if response['dominant_emotion'] is None:
        # Terminamte the function by returning a default string
        return "Invalid text! Please try again!"
    # Set the final string to display in the interface
    final_string = "For the given statement, the system response is "

    # Initialize 'count' by 0
    count = 0

    # Initialize 'length' by the length of the 'response' dictionary
    length = len(response)

    # Make a loop and iterate through each emotion and
    # find the dominant emotion
    for key, value in response.items():
        # If it is the last element in the dictionary, then...
        if count == (length - 1):
            # Print the dominant emotion
            final_string += f"The dominant emotion is '{value}'."
        # Else, if it is the second-to-last element, then...
        elif count == (length - 2):
            # Add 'and' at the beginning and a full-stop at the end before appending
            final_string += f"and '{key}': {value}. "
        #Else, by default...
        else:
            # Add a comma at the end
            final_string += f"'{key}': {value}, "
        # Increment the value of 'count' by 1
        count = count + 1

    # Returning the final text
    return final_string

@app.route("/") #Set the route of the app
def render_index_page():
    '''
    Define the rendering
    '''
    return render_template("index.html") # Render the interface on the 'index.html' page

if __name__ == "__main__": # If this script is the main file, then...
    app.run(host="0.0.0.0", port=5000) # Run the app
