# My Django Template

1. Create python env .
2. Install Django .
3. Create new folder for project and inside do:
   `$ django-admin startproject --template=https://github.com/Z4RD0Z/DjangoTemplate/zipball/master your_cookiecutter.project_name .` .
4. Create new secret key
   `$ python -c 'from django.core.management.utils import get_random_secret_key; \ print(get_random_secret_key())` .
