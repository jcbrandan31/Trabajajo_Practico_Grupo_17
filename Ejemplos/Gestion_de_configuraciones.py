import click
import configparser

@click.group()
def cli():
    """Un simple gestor de configuraciones."""
    pass

@click.command()
@click.argument('file')
@click.argument('section')
@click.argument('option')
def read(file, section, option):
    """Leer una configuración."""
    config = configparser.ConfigParser()
    config.read(file)
    value = config.get(section, option)
    click.echo(f'{section}.{option} = {value}')

@click.command()
@click.argument('file')
@click.argument('section')
@click.argument('option')
@click.argument('value')
def write(file, section, option, value):
    """Escribir una configuración."""
    config = configparser.ConfigParser()
    config.read(file)
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, option, value)
    with open(file, 'w') as configfile:
        config.write(configfile)
    click.echo(f'{section}.{option} escrito con valor {value}')

@click.command()
@click.argument('file')
def list(file):
    """Listar todas las configuraciones."""
    config = configparser.ConfigParser()
    config.read(file)
    for section in config.sections():
        click.echo(f'[{section}]')
        for option in config.options(section):
            value = config.get(section, option)
            click.echo(f'{option} = {value}')
        click.echo()

cli.add_command(read)
cli.add_command(write)
cli.add_command(list)

if __name__ == '__main__':
    cli()
