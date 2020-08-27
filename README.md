# mega-tutorial-flask
virtualenv venv 

pip3.8 install flask

pip3.8 install flask-sqlalchemy

pip3.8 install flask-wtf

pip3.8 install flask-login

pip3.8 install flask-bootstrap

# migrate database
pip3.8 install flask-migrate

flask db init

flask db migrate -m "users table"

flask db upgrade


# email-support
pip3.8 install flask-mail

pip3.8 install pyjwt

pip3.8 install email-validator

# dates & times
pip3.8 install flask-moment

# tranlation with babel
pip3.8 install flask-babel

/for extracting changes/(venv) $ pybabel extract -F babel.cfg -k _l -o messages.pot

/make direction for changed words/(venv) $ pybabel init -i messages.pot -d app/translations -l es

/for updating changes you may use/

(venv) $ pybabel extract -F babel.cfg -k _l -o messages.pot .
(venv) $ pybabel update -i messages.pot -d app/translations
