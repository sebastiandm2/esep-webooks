import os
import requests

def lambda_handler(event, context):
    endpoint = os.environ['SLACK_URL']
    payload = "{{'text':'Issue Created: {}'}}".format(event['issue']['html_url']);
    r = requests.post(url = endpoint, data = payload)
    return { 
        'message' : 'Issue posted to Slack!'
    }