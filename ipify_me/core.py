import requests
import json


def get_ipify_ip():
    """
    docstring
    """
    response = requests.get('https://api.ipify.org?format=json')
    ip = json.loads(response.content)['ip']
    print("Your external IP is " + ip)
