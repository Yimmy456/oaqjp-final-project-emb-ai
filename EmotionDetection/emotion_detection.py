import requests # Import the "requests" package
import json # Import the "json" package

def emotion_detector(text_to_analyze): # Define the "emotion_detector" function

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # Initialize the URL

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # initialize the header

    myobj = {"raw_document": {"text": text_to_analyze}} # Initialize thre variable

    response = requests.post(url, json = myobj, headers = header) # Initialize the response

    if response.status_code == 400: # If the status code of the response is equal to 400, then...
        
        final_dict = { # Initialize a dictionary and set its values to 'None'

            'anger': None, # 1. Set the value of 'anger' to 'None'

            'disgust': None, # 2. Set the value of 'disgust' to 'None'

            'fear': None, # 3. Set the value of 'fear' to 'None'

            'joy': None, # 4. Set the value of 'joy' to 'None'

            'sadness': None, # 5. Set the value of 'sadness' to 'None'

            'dominant_emotion': None # 6. Set the value of 'dominant_emotion' to 'None'
        }

        return final_dict # Return a dictionary with all the values set to 'None'
    
    formatted_response = json.loads(response.text) # Format the response via json

    emotion_list = formatted_response['emotionPredictions'][0]['emotion'] # Store the list of emotions in a variable

    # Store the values of the emotions' scores

    anger_score = emotion_list['anger'] # Store the anger score in a variable

    disgust_score = emotion_list['disgust'] # Store the disgust score in a variable

    fear_score = emotion_list['fear'] # Store the fear score in a variable

    joy_score = emotion_list['joy'] # Store the joy score in a variable

    sadness_score = emotion_list['sadness'] # Store the sadness score in a variable

    # Evaluate to see which emotion has the highest score

    dominant_value = anger_score # Initialize a float to store the emotion with the highest score (Start with the score of 'anger'.)
    
    dominant_emotion = 'anger' # Initialize a string to store the name of the emotion with the highest score (Start with 'anger'.)

    if disgust_score > dominant_value: # If the score of 'disgust' is higher than the value of 'dominant_value'
        
        dominant_value = disgust_score # Then change the value of 'dominant_value' into the score of 'disgust'

        dominant_emotion = 'disgust' # Then change the value of 'dominant_emotion' into 'disgust'


    
    if fear_score > dominant_value: # If the score of 'fear' is higher than the value of 'dominant_value'
        
        dominant_value = fear_score # Then change the value of 'dominant_value' into the score of 'fear'

        dominant_emotion = 'fear' # Then change the value of 'dominant_emotion' into 'fear'


    
    if joy_score > dominant_value: # If the score of 'joy' is higher than the value of 'dominant_value'
        
        dominant_value = joy_score # Then change the value of 'dominant_value' into the score of 'joy'

        dominant_emotion = 'joy' # Then change the value of 'dominant_emotion' into 'joy'


    
    if sadness_score > dominant_value: # If the score of 'sadness' is higher than the value of 'dominant_value'
        
        dominant_value = sadness_score # Then change the value of 'dominant_value' into the score of 'sadness'

        dominant_emotion = 'sadness' # Then change the value of 'dominant_emotion' into 'sadness'


    
    final_dict = { # Initialize the final dictionary to store 1. the scores of the emotions; and 2. the name of the most dominant emotion
        
        'anger': anger_score, # 1. Store the score for 'anger' as a value in the index where its key is 'anger'

        'disgust': disgust_score, # 2. Store the score for 'disgust' as a value in the index where its key is 'disgust'

        'fear': fear_score, # 3. Store the score for 'fear' as a value in the index where its key is 'fear'

        'joy': joy_score, # 4. Store the score for 'joy' as a value in the index where its key is 'joy'

        'sadness': sadness_score, # 5. Store the score for 'sadness' as a value in the index where its key is 'sadness'

        'dominant_emotion': dominant_emotion # 6. Store the name of the most dominant emotion as a value in the index where its key is 'dominant_emotion'

    }

    return final_dict # Return the final dictionary