
# Site contains:
### Work with DB
### Registration, login, logout
### Pagination
### Cookies,sessions
### Security certificate( https )

-------------
# Installation


1. - clone the project
 ```
  git clone https://github.com/immmmmortal/BEDOLAGA_SITE.git
 ```
2. - create and start a a virtual environment
 ```
   virtualenv env --no-site-packages
   source env/bin/activate
 ```
3. - Install the project dependencies:
```
   pip install -r requirements.txt
```
4. - Create .env
```
   touch .env
```
5. - obtain a secret from [MiniWebTool](https://miniwebtool.com/django-secret-key-generator/) key and add to secrets.sh
6. - add secret to .env
7. - add .env to .gitignore file
8. - then run
```
   python manage.py migrate
```
9 - To create admin account
```
    python manage.py createsuperuser
```
10.- Then to makemigrations for the app
```
    python manage.py makemigrations phonestore
```
11. - Again run migrate
```
   python manage.py migrate
 ```
12. - Project readt for development, to start the development server run:
```
    python manage.py runserver_plus --cert-file ./localhost.crt localhost:8000 --keep-meta-shutdown

```
