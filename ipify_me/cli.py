"""Console script for ipify_me."""
import sys
import click
from ipify_me import core 

@click.command()
def main(args=None):
    core.get_ipify_ip()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
