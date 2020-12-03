import requests
import json


def ipify_me():
    """
    docstring
    """
    response = requests.get('https://api.ipify.org?format=json')
    ip = json.loads(response.content)['ip']
    print("Your external IP is " + ip)

