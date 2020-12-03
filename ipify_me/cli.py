"""Console script for ipify_me."""
import sys
import click
import requests
import json


@click.command()
def main(args=None):
    """Console script for ipify_me."""
    response = requests.get('https://api.ipify.org?format=json')
    ip = json.loads(response.content)['ip']
    print("Your external IP is " + ip)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
