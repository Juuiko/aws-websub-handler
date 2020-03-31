import json
import requests

def lambda_handler(event, context):

    url = 'https://www.w3schools.com/python/demopage.php'
    myobj = {'somekey': 'somevalue'}

    x = requests.post(url, data = myobj)

    print(x.text)

    return {
        'statusCode': 200,
        'body': event
    }
