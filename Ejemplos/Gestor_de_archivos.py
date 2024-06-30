import click
import os
import shutil

@click.group()
def cli():
    """Un simple gestor de archivos."""
    pass

@click.command()
@click.argument('filename')
def touch(filename):
    """Crear un nuevo archivo llamado FILENAME."""
    with open(filename, 'w') as f:
        pass
    click.echo(f'Archivo "{filename}" creado.')

@click.command()
@click.argument('dirname')
def mkdir(dirname):
    """Crear un nuevo directorio llamado DIRNAME."""
    os.makedirs(dirname, exist_ok=True)
    click.echo(f'Directorio "{dirname}" creado.')

@click.command()
@click.argument('path')
def ls(path='.'):
    """Listar el contenido de PATH."""
    for item in os.listdir(path):
        click.echo(item)

@click.command()
@click.argument('src')
@click.argument('dst')
def cp(src, dst):
    """Copiar SRC a DST."""
    shutil.copy(src, dst)
    click.echo(f'Copiado "{src}" a "{dst}".')

@click.command()
@click.argument('src')
@click.argument('dst')
def mv(src, dst):
    """Mover SRC a DST."""
    shutil.move(src, dst)
    click.echo(f'Movido "{src}" a "{dst}".')

@click.command()
@click.argument('path')
def rm(path):
    """Eliminar el archivo o directorio en PATH."""
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)
    click.echo(f'Eliminado "{path}".')

cli.add_command(touch)
cli.add_command(mkdir)
cli.add_command(ls)
cli.add_command(cp)
cli.add_command(mv)
cli.add_command(rm)

if __name__ == '__main__':
    cli()
