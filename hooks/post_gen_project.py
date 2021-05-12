import os


def generate_secret_key():
    """"""
    return "assdsadsadsajsajkdsakdjsakjdkKDKASJDk"
    #TODO


def set_secret_key():
    """"""

    secret_key = generate_secret_key()

    with open(
            "../{{cookiecutter.project_dirname}}/{{cookiecutter.project_name}}/settings.py",
            "r+") as f:

        file_contents = f.read().replace("!!!DJANGO_SECRET_KEY HERE!!!",
                                         secret_key)
        f.seek(0)
        f.write(file_contents)
        f.truncate()


def main():
    """"""
    set_secret_key()


if __name__ == "__main__":
    main()