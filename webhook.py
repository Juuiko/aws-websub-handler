import json
import requests
import xml.etree.ElementTree as ET

def lambda_handler(event, context):
    if event['requestContext']['http']['method'] == 'GET':
        challenge = event['queryStringParameters']['hub.challenge']
        return challenge
    else:
        body = event['body']
        if event['requestContext']['http']['path'] == '/default/webhook-generator':
            body = body.replace("\\","")
            xml = ET.fromstring(body)

            if list(xml[0].attrib)[0] == "rel":
                videoURL = "https://youtu.be/" + xml[4][1].text
                username = xml[4][5][0].text
                content = "[" + username + " just uploaded a new video!](" + videoURL + ")"
                data = {
                    'username': "Youtube",
                    'content': content
                }
                requests.post(*WEBHOOK_URL*, json.dumps(data), headers={"Content-Type": "application/json"})
        tData = json.loads(body)
            if len(tData['data'])>0:
                channel = tData['data'][0]
                channelLink = "https://www.twitch.tv/" + channel['user_name']
                gameTitleURL = "https://api.twitch.tv/helix/games?id=" + channel['game_id']
                gameTitle = requests.get(gameTitleURL, headers = {'Client-ID': 'quk4bsuua611lzukiwsxc9bx0ccuj4'})
                text = channel['user_name'] + " is streaming " + gameTitle.json()['data'][0]['name'] + "!\n" + channel['title'] + "\n" + channelLink
                data = {
                    'username': "Twitch",
                    'content': text
                }
            requests.post(*WEBHOOK_URL*, json.dumps(data), headers={"Content-Type": "application/json"})
