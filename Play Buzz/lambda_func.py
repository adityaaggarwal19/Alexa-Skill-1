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
    if intentName == "buzzfuz":
        return fuzbuzz(intent, session)
    elif intentName == "buz":
        return fuzstart(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser():
    import random
    o = [3,5,6,7,8,9]
    a=random.choice(o)
    i[0]=a
    sessionAttributes = {}
    for k in range(0,100):
        if i[0] == int(val[k]/10):
            arr[k]=1
        elif i[0] == int(val[k]%10):
            arr[k]=1
        elif int(val[k]%i[0]) == 0:
            arr[k]=1
        else:
            arr[k]=0   
    cardTitle = " Hello"
    speechOutput =  "Hello , Welcome to buzz! " \
                    "Say BUZZ when you find a number having "+ str(i[0]) + " or multiple of " + str(a) +" otherwise say the number"\
                    " Say START when ready"
    repromptText =  "Hello , Welcome to buzz! " \
                    "Say BUZZ when you find a number having "+ str(i[0]) + " or multiple of " + str(a) +" otherwise say the number"\
                    " Say START when ready"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))




def fuzbuzz(intent, session):
    sessionAttributes = {}
    cardTitle = " Hello"
    speechOutput="0"
    i[1]=1
    repromptText ="0"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def fuzstart(intent, session):
    cardTitle = intent['name']
    sessionAttributes = {}
    
    if i[1] == 99 or i[1] == 98:
        speechOutput="CONGRATS! You Won"
    elif 'num' in intent['slots']:
        c=intent['slots']['num']['value']
        if c.isdigit() or c=="buzz" or c=="buz":
            if arr[i[1]]==0:
                if int(c) == val[i[1]]:
                    if arr[i[1]+1]==0:
                        speechOutput=str(int(c)+1)
                    elif arr[i[1]+1]==1:
                        speechOutput="BUZZ"
                else:
                    speechOutput="OOPS! YOU LOSE"
                i[1]=i[1]+2
            elif arr[i[1]]==1:
                if c=="buzz" or c=="buz" or c=="bus" or c=="zz":
                    if arr[i[1]+1]==0:
                        speechOutput=str(val[i[1]+1])
                    elif arr[i[1]+1]==1:
                        speechOutput="BUZZ"
                else:
                    speechOutput="OOPS! YOU LOSE"
                i[1]=i[1]+2
        else:
            speechOutput="please say a number"
    else:
        speechOutput="please say a number"
    
    repromptText = "I'm not sure what your number is. " 
    shouldEndSession = False                
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))
 




def handleSessionEndRequest():
    cardTitle = "Session Ended"
    speechOutput = "Thank you for using logos facts Alexa Skills Kit. " \
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


def buildResponse(sessionAttr , speechlet):
    return {
        'version': '1.0',
        'sessionAttributes': sessionAttr,
        'response': speechlet
    }
i=[0,0]
val=list(range(0,100))
arr=[0]*100
