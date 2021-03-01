pip3.8 install virtualenv 

(Library to setup virtual enviorments for proyects. It enables a proyect from using the an specific python version.)

virtualenv venv --python=python3.8

(Setup the virtual enviorment version)

source venv/bin/activate
(Use the virtual enviorment)

deactivate
(Leave virtual enviorment)

pip install Flask-RESTful

(lint with virtualenv)[https://pypi.org/project/pylint-venv/]

pip install Flask-JWT