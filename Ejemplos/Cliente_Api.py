import click
import requests

@click.group()
def cli():
    """Un simple cliente API."""
    pass

@click.command()
@click.argument('url')
def get(url):
    """Realizar una solicitud GET a URL."""
    response = requests.get(url)
    click.echo(response.text)

@click.command()
@click.argument('url')
@click.argument('data', required=False)
def post(url, data=None):
    """Realizar una solicitud POST a URL con DATA."""
    response = requests.post(url, data=data)
    click.echo(response.text)

@click.command()
@click.argument('url')
@click.argument('data', required=False)
def put(url, data=None):
    """Realizar una solicitud PUT a URL con DATA."""
    response = requests.put(url, data=data)
    click.echo(response.text)

@click.command()
@click.argument('url')
def delete(url):
    """Realizar una solicitud DELETE a URL."""
    response = requests.delete(url)
    click.echo(response.text)

cli.add_command(get)
cli.add_command(post)
cli.add_command(put)
cli.add_command(delete)

if __name__ == '__main__':
    cli()
