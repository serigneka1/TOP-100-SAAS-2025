import click
import os

@click.command()
@click.option('--cred', envvar='GOOGLE_APPLICATION_CREDENTIALS', help='Chemin vers le fichier de clé JSON GCP')
def authenticate(cred):
    if not os.path.exists(cred):
        click.echo(f"Fichier introuvable : {cred}")
        return

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred
    click.echo(f"Authentifié avec : {cred}")

if __name__ == '__main__':
    authenticate()
