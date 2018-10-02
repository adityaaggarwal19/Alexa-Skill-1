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
    if intentName == "whatislogosfacts":
        return logos_facts(intent, session)
    elif intentName == "AMAZON.HelpIntent":
        return welcomeuser()
    elif intentName == "AMAZON.CancelIntent" or intentName == "AMAZON.StopIntent":
        return handleSessionEndRequest()
    else:
        raise ValueError("Invalid intent")

def onSessionEnd(sessionEndedRequest, session):
    print("on_session_ended requestId=" + sessionEndedRequest['requestId'] + ", sessionId=" + session['sessionId'])

def welcomeuser():
    sessionAttributes = {}
    cardTitle = " Hello"
    speechOutput =  "Hello , Welcome to logos facts! " \
                    "You can know interesting facts about logos by saying Tell me logos facts"
    repromptText =  "You can know interesting facts about logos by saying Tell me logos facts"
    shouldEndSession = False
    
    return buildResponse(sessionAttributes, buildSpeechletResponse(cardTitle, speechOutput, repromptText, shouldEndSession))

def logos_facts(intent, session):
    import random
    index = random.randint(0,len(logo)-1)
    cardTitle = intent['name']
    sessionAttributes = {}
    speechOutput = "Logo fact is that " + logo[index] 
    repromptText = "You can know interesting facts about logos by saying Tell me logos facts"
    shouldEndSession = True                   
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



logo = [ "The 'VA' of the sony VAIO logo has been made to look like an analogue signal wave like pattern and the ‘IO’ resembles the binary number system 1 and 0." ,
          "The Baskin BR Robbins ice cream chain offer a variety of 31 different flavours so the number 31 has been incorporated within the 'B' and 'R' intials in pink." ,
          "Amazon has the ultimate shopping destination with access to every product hence the logo consists of a yellow arrowed smiley that extends from a to z.",
          "CISCO the company based in San Francisco rightfully decided to name themselves after the city hence the logo is inspired by San Francisco’s famous architectural wonder, the Golden Gate bridge." ,
          "In F1 (formula 1)'s logo we see is a bold black ‘F’ and a red streak of speed lines with the white mid-section hidden numeral 1" ,
          "Wikipedia is one of the frequently used sites with its globe logo made up of jigsaw puzzles inscribed with letters from various written systems which is unfinished to symbolize that data gathering is ever-growing and Wikipedia is a work-in-progress." ,
          "The FedEx logo has an intentionally hidden white arrow between the letters 'E' and 'x' that was created by blending two different fonts together. It has won over 40 design awards and is renowned for the best use of negative space.",
          "VLC Media Player uses a traffic cone as its logo because the students who wrote the code for the VideoLAN project had a traffic cone collection." ,
          "The logo for Domino’s Pizza has three dots because there were only three original Domino’s stores in 1965. They planned to add a new dot for every new store, but the idea was dropped due to the fast growth of the franchise." ,
          "The logo for Bluetooth, which was named after the Danish King Harald Bluetooth, is derived from the Danish letters that represent the king’s initials – H (ᚼ) and B (ᛒ)." ,
          "The Ferrari prancing horse logo originally decorated the plane of Count Francesco Baracca, Italy’s top fighter ace of WWI. After Francesco was shot down, his mother said to Enzo Ferrari, Ferrari, put my son’s prancing horse on your cars. It will bring you good luck",
          "As opposed to popular belief, McDonald’s golden 'M' logo does not come from the name McDonald’s. It, in fact, comes from the golden architectural arches that were part of the first McDonald’s restaurant" ,
          "At first glance, the dark pink logo for LG Electronics looks like a winking face. But if you look a little closer, you'll see the face's nose is an L and the outline of the 'face' is a 'G' Some fans have even noted a similarity between LG's logo and a modified Pacman." ,
          "The logo on The Hershey Company's Hershey's Kisses product has a hidden logo: an extra Kiss. Turn your head to the left and you'll see that between the 'K' and the 'I' there is a Hershey's Kiss baked into the logo. " ,
          "NBC’s logo is a peacock, When the logo was developed color televisions were being introduced (explaining the rainbow of colors), and the network wanted a logo that would cause black and white tv owners to make the switch. So, they went with the common phrase (at the time), ‘proud as a peacock’, promoting that they were proud of their new color system.",
          "Picasa, Google’s image organizer and editor, has an interesting logo mark. At first glance it looks like a simple camera shutter, but the negative space in the center of the shutter actually forms a house. This is because Picasa is considered ‘home’ for all of your photos, and casa in Spanish means home.",
          "My Fonts is an online font resource, allowing users to access a number of fonts. The ‘My’ in My Fonts is stylized to look like a hand, giving the impression that users can get their hands on whatever fonts they’d like.",
          "The Tour De France logo has two hidden messages first with a cyclist making up the letter ‘r’, but the second is the yellow circle that acts as the bike’s wheel is also a sun, indicating that the events of the race only occur in the daytime.",
          "Sun Microsystems was a technological company. The diamond shaped logo isn’t just just a bunch of squiggly lines, but is actually comprised of ‘u’s and ‘n’s. Some of the letters are stacked on top of each other, creating the letter ‘s’. All of this put together spells out ‘sun’ over and over.",
          "Pittsburgh zoo logo looks like a simple tree at first glance. If you look in the negative space, though, you’ll see the profiles of both a gorilla and a lion facing each other.",
          "The popular chocolate bar, Toblerone, has been around for quite some time. It’s current logo features a mountain, symbolizing the Matterhorn Mountain in Switzerland. Hidden inside the mountain is a bear, symbolizing the unique honey flavor found in the chocolate and the fact that the chocolate is made in the ‘City of Bears’." ,
          "Toyota’s current logo has been around since 1990. The popular car manufacturer’s three overlapping rings symbolize the unification of the hearts of Toyota customers and Toyota’s products." ,
          "Audi the four rings represent the four companies that came together to create the original Audi, Auto Union." ,
          "Google’s logo is supposed to symbolize that they don’t play by the rules and know how to have fun. Instead of having a crazy font or symbol, they chose to relay their message with color. They stuck with the primary color pallette, but broke it with a secondary color, green." ,
          "Gillette, a razor company, is razor sharp with their logo — literally. The intricate and precise cut in the ‘G’ and ‘i’ look as though they’ve been carefully removed with an extra sharp Gillette razor." ,
          "Pinterest got its namesake from the idea of ‘pinning’ things you like to a board. To further the idea of the pin, the ‘P’ represents a pushpin. This brings together the real life aspect of tacking something to your wall and also doing it in the digital age." ,
          "Adidas is a popular sports apparel and shoe company. Three stripes have always been a part of their logo, but in their most recent redesign the stripes are staggered to look like a mountain. The mountain represents the challenges and obstacles athletes will face and overcome." ,
          "IBM’s famous logo is globally recognized. The white stripes passing through the letterforms give the illusion of equal signs in the lower areas of the letters, which represents equality.",
          "Many people are inclined to think that the logo of the South Korean conglomerate Hyundai is simply the first letter of its name. But actually, the letter ’Н’ symbolises two people (a client and a representative of the company) shaking hands." ,
          "Mosleep is an organization of doctors that deals with people having sleeping disorders. The logo is their intial ‘M’ that was designed to also look like a bed. ",
        "The Microsoft logo depicts four colours, each representing an independent component. The blue square represents Windows. The red represents office. The green represents Xbox, in other words, fun. And the yellow represents the surface. Though no evidence justifying the choice of yellow is known.",
        "HP-The Hewlett Packard logo combines the surname of both its founders. The blue colour in the logo describes excellence whereas the white prompts grace. The tailing out of H and P in the logo symbolises innovation."
        ]
