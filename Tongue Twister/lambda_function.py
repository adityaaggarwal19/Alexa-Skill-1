def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest" :
        return onLaunch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest" :
        return onIntent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest" :
        return onSessionEnd(event['request'], event['session'])
def onLaunch(launchRequest, session):
    return welcomeuser()

def onIntent(intentRequest, session):
    intent = intentRequest['intent']
    intentName = intentRequest['intent']['name']
    if intentName == "twister":
        return twist_tongue(intent, session)
    elif intentName == "AMAZON.RepeatIntent":
        return handlerepeat(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def handlerepeat(intent, session):
    for i in range(len(tt)):
        if tt[i][1] == 1:
            index=i
    speechOutput = "Try and speak, " + tt[index][0]  
    cardTitle = " Hello"
    repromptText = "You can know interesting tongue twisters by saying Tell me tongue twister"
    should_end_session = False
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, repromptText, should_end_session))

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello"
    speechOutput =  "Hello , Welcome to twist my tongue! " \
                    "You can know interesting tongue twisters by saying Tell me tongue twister"
    repromptText =  "You can know interesting tongue twisters by saying Tell me tongue twister"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def twist_tongue(intent, session):
    for i in range(len(tt)):
        tt[i][1]=0
    import random
    index = random.randint(0,len(tt)-1)
    cardTitle = intent['name']
    speechOutput = "Try and speak, " + tt[index][0] 
    tt[index][1]=1
    repromptText = "You can know interesting tongue twisters by saying Tell me tongue twister"
    shouldEndSession = False      
    sessionAttributes = {"speechOutput": speechOutput,
                         "repromptText": repromptText,
                        }
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))
        
def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using twist my tongue Alexa Skills Kit. " \
                    "Have a great time! "
    shouldEndSession = True
    return buildResponse({}, buildSpeechletResponse(cardTitle, speechOutput, None, shouldEndSession))

def buildSpeechletResponse(title, output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
            
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
            },
            
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }
def buildResponseWithoutCard(output, repromptTxt, endSession):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
            },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': repromptTxt
                }
            },
        'shouldEndSession': endSession
    }

def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }



tt = [ ["Peter Piper picked a peck of pickled peppers. How many pickled peppers did Peter Piper pick?",0],
["Can you can a can as a canner can can a can?",0],
["I wish to wish the wish you wish to wish, but if you wish the wish the witch wishes, I won't wish the wish you wish to wish.",0],
["Picky people pick Peter Pan Peanut-Butter, 'tis the peanut-butter picky people pick.",0],
["I scream, you scream, we all scream for icecream!",0],
["Thirty-three thirsty, thundering thoroughbreds thumped Mr. Thurber on Thursday.",0],
["She saw Sharif's shoes on the sofa. But was she so sure those were Sharif's shoes she saw?",0],
["She sells seashells by the seashore",0],
["Susie works in a shoeshine shop. Where she shines she sits, and where she sits she shines",0],
["I slit the sheet, the sheet I slit, and on the slitted sheet I sit",0],
["Lesser leather never weathered wetter weather better",0],
["Gobbling gorgoyles gobbled gobbling goblins.",0],
["Six sleek swans swam swiftly southwards",0],
["How many cookies could a good cook cook If a good cook could cook cookies? A good cook could cook as much cookies as a good cook who could cook cookies.",0],
["How much pot, could a pot roast roast, if a pot roast could roast pot.",0],
["Six slimy snails sailed silently.",0],
["The great Greek grape growers grow great Greek grapes.",0],
["Singing Sammy sung songs on sinking sand.",0],
["I wish to wash my Irish wristwatch.",0],
["On a lazy laser raiser lies a laser ray eraser.",0],
["He threw three free throws.",0],
["Chester Cheetah chews a chunk of cheep cheddar cheese.",0],
["Sounding by sound is a sound method of sounding sounds.",0]
        ]
