import json
import requests
import xml.etree.ElementTree as ET

def lambda_handler(event, context):
    if event['requestContext']['http']['method'] == 'GET':
        challenge = event['queryStringParameters']['hub.challenge']
        return challenge
    else:                           #if POST
        body = event['body']
        if body[0] == "<":          #if youtube xml
            body = body.replace("\\","")
            xml = ET.fromstring(body)

            if list(xml[0].attrib)[0] == "rel":
                videoURL = "https://youtu.be/" + xml[4][1].text
                username = xml[4][5][0].text
                content = "[" + username + " just uploaded a new video!](" + videoURL + ")"
                url = 'https://discordapp.com/api/webhooks/691028975803170858/yIT3IOLjqdGzUXZ28TOwzc5Aew5Rb8H6X2kzsZhHQ7-5rgaer_FP36o6_3N5ElyGK-rD'
                data = {
                    'username': "Youtube",
                    'content': content
                }
                requests.post(url, json.dumps(data), headers={"Content-Type": "application/json"})
        else:
            print("Twitch!")
        return