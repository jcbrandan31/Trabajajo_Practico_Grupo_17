Python 3.8.9 (tags/v3.8.9:a743f81, Apr  6 2021, 14:02:34) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import click

tasks = []

@click.group()
def cli():
    """Un simple gestor de tareas."""
    pass

@click.command()
@click.argument('description')
def add(description):
    """Añadir una nueva tarea con DESCRIPCIÓN."""
    tasks.append({'description': description, 'completed': False})
    click.echo(f'Tarea "{description}" añadida.')

@click.command()
def list():
    """Listar todas las tareas."""
    if not tasks:
        click.echo("No hay tareas.")
        return
    for i, task in enumerate(tasks):
        status = '✔' if task['completed'] else '✘'
        click.echo(f"{i+1}. [{status}] {task['description']}")

@click.command()
@click.argument('task_id', type=int)
def complete(task_id):
    """Marcar la tarea con TASK_ID como completada."""
    try:
        task = tasks[task_id - 1]
        task['completed'] = True
        click.echo(f'Tarea "{task["description"]}" marcada como completada.')
    except IndexError:
        click.echo('ID de tarea no válido.')

@click.command()
@click.argument('task_id', type=int)
def delete(task_id):
    """Eliminar la tarea con TASK_ID."""
    try:
        task = tasks.pop(task_id - 1)
        click.echo(f'Tarea "{task["description"]}" eliminada.')
    except IndexError:
        click.echo('ID de tarea no válido.')

cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)

if __name__ == '__main__':
    cli()
