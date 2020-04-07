import json
import requests
import xml.etree.ElementTree as ET

def lambda_handler(event, context):
    if event['requestContext']['http']['method'] == 'GET':
        challenge = event['queryStringParameters']['hub.challenge']
        print(event)
        return challenge
    else:
        body = event['body']
        root = ET.fromstring(body)
        if root[2].text == "YouTube video feed":
            username = root[4][5][0].text
            videoURL = "https://youtu.be/" + root[4][1].text
            content = username + " just uploaded a new video!\n" + videoURL
            url = 'https://discordapp.com/api/webhooks/694272177909792768/ab_xjeEZ8Zf5V7_7l7Y3OL6UH6b3a6NdWKFVFLfLcmNqueMQrncF_jJsKh1EkjyEhJ8p'
            data = {
                'username': "Quantex Bot",
                'content': content
            }
            requests.post(url, json.dumps(data), headers={"Content-Type": "application/json"})
        else:
            print(root[2].text)
        return "ACK"
