from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Wildlife Guru. " \
                    "Please tell me your choice one product second animal and third ngo names if product then by saying, " \
                    "my option is one"
    reprompt_text = "Please tell me your choice by saying, " \
                    "my option is one."
    
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using Wildlife Guru. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def set_option(intent, session):

    card_title = "Menu Option"
    session_attributes = {}
    should_end_session = False

    if 'opt' in intent['slots']:
        user_choice = intent['slots']['opt']['value']
        #session_attributes = create_favorite_color_attributes(favorite_color)
        if user_choice == "1"
            speech_output = "Your choice is product. " \
                            "You can ask me about product by saying, " \
                            "tell me about necklace?"
            reprompt_text = "You can ask me about product by saying, " \
                            "tell me about necklace?"
        elif user_choice == "2":
            speech_output = "I now know your choice is "  \
                            "Animal" \
                            ". You can ask me about animal by saying, " \
                            "tell me about animal name?"
            reprompt_text = "You can ask me about animal by saying, " \
                            "tell me about animal name?"
        elif user_choice == "3":
            speech_output = "I now know your choice is " \
                            "ngo names"  \
                            ". You can ask me about ngos by saying, " \
                            "tell me about ngos name?"
            reprompt_text = "You can ask me about ngos by saying, " \
                            "tell me about ngos name?"
        else:
            speech_output = "I'm not sure what your choice is. "+ \
                            user_choice +" Please try again."
            reprompt_text = "I'm not sure what your choice is. " \
                            "You can tell me your choice by saying, " \
                            "my option is one."
    else:
        speech_output = "I'm not sure what your choice is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your choice is. " \
                            "You can tell me your choice by saying, " \
                            "my option is one."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def know_product(intent, session):
    card_title = "Product Details"
    session_attributes = {}
    should_end_session = False

    if 'typeof' in intent['slots']:
        user_product = intent['slots']['typeof']['value']
        #session_attributes = create_favorite_color_attributes(favorite_color)
        if user_product == "necklace":
            speech_output = "Your product is necklace. " \
                            "You can ask me about necklace by saying, " \
                            "tell me about necklace?"
            reprompt_text = "You can ask me about necklace by saying, " \
                            "tell me about necklace?"
        elif user_product == "medicines":
            speech_output = "Your product is medicines "  \
                            ". You can ask me about medicines by saying, " \
                            "tell me about medicines?"
            reprompt_text = "You can ask me about medicines by saying, " \
                            "tell me about medicines?"
        else:
            speech_output = "I'm not sure what your product is. "+ \
                            user_product +" Please try again."
            reprompt_text = "I'm not sure what your product is. " \
                            "You can tell me your product by saying, " \
                            "my product is necklace."
    else:
        speech_output = "I'm not sure what your product is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your choice is. " \
                            "You can tell me your choice by saying, " \
                            "my option is one."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
 
def get_names():
    names = ""
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
    table = dynamodb.Table('sanct')
    response = table.scan()
    nameCount == len(response['city'])
    for idx, item in enumerate(response['city']):
        names += item['name']
        if idx == nameCount - 2:
            names += " and "
        else if idx != nameCount - 1:
            names += ", "
    return names

def know_animal(intent, session):
    card_title = "Animal Details"
    session_attributes = {}
    should_end_session = False

    if 'animal' in intent['slots']:
        user_animal = intent['slots']['animal']['value']
        #session_attributes = create_favorite_color_attributes(favorite_color)
        speech_output=get_names()
        '''
        speech_output = "Your animal is " + \
                        user_animal + ". You can ask me about animal by saying, " \
        '''                    "tell me about elephant?"
        reprompt_text = "You can ask me about animal by saying, " \
                            "tell me about elephant?"
        
    else:
        speech_output = "I'm not sure what your animal is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your animal is. " \
                            "You can tell me your animal by saying, " \
                            "tell me about elephant."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))        

def wild_fact(intent, session):
    import random
    index = random.randint(0,len(wild)-1)
    cardTitle = "Wildlife Facts"
    sessionAttributes = {}
    should_end_session = False
    speechOutput = "One of the interesting fact related to wildlife is " + wild[index] 
    repromptText = "You can know interesting facts about wildlife like by saying Tell me about wildlife"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def ngo_details(intent, session):
    cardTitle = "NGO Details"
    sessionAttributes = {}
    should_end_session = False
    speechOutput = "NGO Details are here" 
    repromptText = "You can know details about NGO by saying Tell me about NGO"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def movie_details(intent, session):
    cardTitle = "Movie Details"
    sessionAttributes = {}
    should_end_session = False
    speechOutput = "Movie Details are here" 
    repromptText = "You can know details about NGO by saying Tell me about NGO"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def park_details(intent, session):
    cardTitle = "Park Details"
    sessionAttributes = {}
    should_end_session = False
    speechOutput = "Park Details are here" 
    repromptText = "You can know details about park by saying Tell me about park"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def expert_details(intent, session):
    cardTitle = "Expert Details"
    sessionAttributes = {}
    should_end_session = False
    speechOutput = "Expert Details are here" 
    repromptText = "You can know details about Expert by saying Tell me about Expert"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def game_play(intent, session):
    cardTitle = "Wildlife Game"
    sessionAttributes = {}
    should_end_session = False
    speechOutput = "Games are here" 
    repromptText = "You can play games by saying play wildlife game"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "WhatIsOption":
        return set_option(intent, session)
    elif intent_name == "ProductName":
        return know_product(intent,session)
    elif intent_name == "AnimalName":
        return know_animal(intent,session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name== "WildlifeFacts":
        return wild_fact(intent,session)
    elif intent_name == "NgoName":
        return ngo_details(intent,session)
    elif intent_name == "GamesName":
        return game_play(intent,session)
    elif intent_name == "ExpertName":
        return expert_details(intent,session)
    elif intent_name == "MovieName":
        return movie_details(intent,session)
    elif intent_name == "ParkName":
        return park_details(intent,session)
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
        
wild = [
  'Slugs have four noses.',
  'The fingerprints of a koala are so indistinguishable from humans that they have on occasion been confused at a crime scene.',
  'A snail can sleep for three years.',
  'The heart of a shrimp is located in its head.',
  'Elephants are the only animal that can\'t jump.',
  'A rhinoceros horn is made of hair.',
  'It is possible to hypnotize a frog by placing it on its back and gently stroking its stomach.',
  'It takes a sloth two weeks to digest its food.',
  'Nearly three percent of the ice in Antarctic glaciers is penguin urine.',
  'A cow gives nearly 200,000 glasses of milk in a lifetime.',
  'Bats always turn left when leaving a cave.',
  'Giraffes have no vocal chords.',
  'An ostrich eye is bigger than its brain.',
  'Kangaroos can\'t fart.'
]
