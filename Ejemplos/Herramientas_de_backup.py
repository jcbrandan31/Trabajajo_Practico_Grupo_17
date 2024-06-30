import click
import shutil
import os

@click.group()
def cli():
    """Una simple herramienta de backup."""
    pass

@click.command()
@click.argument('source')
@click.argument('backup')
def backup(source, backup):
    """Crear una copia de seguridad de SOURCE en BACKUP."""
    shutil.copytree(source, backup)
    click.echo(f'Backup de "{source}" creado en "{backup}".')

@click.command()
@click.argument('backup')
@click.argument('destination')
def restore(backup, destination):
    """Restaurar BACKUP en DESTINATION."""
    shutil.copytree(backup, destination)
    click.echo(f'Backup "{backup}" restaurado en "{destination}".')

@click.command()
@click.argument('backup_dir')
def list_backups(backup_dir):
    """Listar todas las copias de seguridad en BACKUP_DIR."""
    backups = os.listdir(backup_dir)
    if not backups:
        click.echo("No hay copias de seguridad disponibles.")
    else:
        for backup in backups:
            click.echo(backup)

cli.add_command(backup)
cli.add_command(restore)
cli.add_command(list_backups)

if __name__ == '__main__':
    cli()
