import requests # Import the "requests" package

def emotion_detector(text_to_analyze): # Define the "emotion_detector" function

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # Initialize the URL

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # initialize the header

    myobj = {"raw_document": {"text": text_to_analyze}} # Initialize thre variable

    response = requests.post(url, json = myobj, headers = header) # Initialize the response

    return response # Return the response