import click
import os


credentials_path = "dataanalytics-457219-b99f0aec4b36.json"
@click.command()
def authenticate():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
    click.echo(f'{os.environ["GOOGLE_APPLICATION_CREDENTIALS"]}!')

if __name__ == '__main__':
    authenticate()