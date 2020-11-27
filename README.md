# myHVACRguide
https://docs.djangoproject.com/fr/2.2/


* Note a toute fin utile :
- creer fichier pip freeze : py -m pip freeze > uninstall.txt
- IntelliSense HTML CTRL+Space

* env. (variable d'environnement directement dans Heroku)
SECRET_KEY=kobl@t=yw9d*0y%jt2gjnq78=u!z_rrxb&w8e47l!(jz@m79zy
DEBUG=False
DB_NAME=your-db-name
DB_USER=your-db-user-name
DB_PASSWORD=your-db-password
DB_HOST=localhost
RECAPTCHA_PUBLIC_KEY=your-recaptcha-public-key
RECAPTCHA_PRIVATE_KEY=your-recaptcha-private-key

* HEROKU
- Creer la base de données
    heroku addons:create heroku-postgresql:hobby-dev
- Commandes
    heroku logs --tail --app myhvacrguide
    heroku config:set DISABLE_COLLECTSTATIC=1 --app myhvacrguide
    heroku run python src/manage.py collectstatic --app myhvacrguide




* TODOLIST
- GCU
https://www.legalplace.fr/contrats/conditions-generales-d-utilisation/creer/11
https://django-termsandconditions.readthedocs.io/en/latest/#

- Accounts
delete profile

- template
404
403
- dashboard
creation
- setting
mise en cache
- menu navigation en python

template error 403


test