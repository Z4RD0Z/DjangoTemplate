import os
import secrets
import subprocess
from pathlib import Path

db = "{{cookiecutter.db}}"


def generate_secret_key():
    """
    Generate Secret key
    """

    length = 50
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

    key = ''.join(secrets.choice(chars) for i in range(length))
    return key


def set_secret_key():
    """
    Add secret key to project settings
    """

    secret_key = generate_secret_key()

    with open(
            "../{{cookiecutter.project_dirname}}/{{cookiecutter.project_name}}/settings.py",
            "r+") as f:

        file_contents = f.read().replace("!!!DJANGO_SECRET_KEY HERE!!!",
                                         secret_key)
        f.seek(0)
        f.write(file_contents)
        f.truncate()


def set_db_settings():
    """[summary]
    """
    db_engine = ""
    if db == "msql":
        db_engine = "django.db.backends.mysql"
    elif db == "postgres":
        db_engine = "django.db.backends.postgresql_psycopg2"

    with open(
            "../{{cookiecutter.project_dirname}}/{{cookiecutter.project_name}}/settings.py",
            "r+") as f:

        file_contents = f.read().replace("CHANGE ENGINE HERE", db_engine)
        f.seek(0)
        f.write(file_contents)
        f.truncate()


def create_env():
    """[summary]
    """
    try:
        subprocess.run(["pyenv", 'install', "{{cookiecutter.python_version}}"])
        subprocess.run([
            'pyenv', 'virtualenv', "{{cookiecutter.python_version}}",
            "{{cookiecutter.project_name}}"
        ])
    except subprocess.CalledProcessError as e:
        print(e.output)


def install_requirements():
    """[summary]
    """
    try:
        venv_dir = f"{Path.home()}/.pyenv/versions/django"

        pip = os.path.join(venv_dir, 'bin', 'pip')

        subprocess.run(args=[
            pip, 'install', '-r',
            '../{{cookiecutter.project_dirname}}/requirements.txt'
        ])
    except subprocess.CalledProcessError as e:
        print(e.output)


def main():
    """"""
    set_secret_key()
    set_db_settings()
    create_env()
    install_requirements()


if __name__ == "__main__":
    main()