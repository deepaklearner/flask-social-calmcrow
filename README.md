# App

python -m venv venv
venv\Scripts\activate
or
.\venv\Scripts\activate.bat

Linus:
source ./env/bin/Activate

In windows:
set FLASK_APP=calmcrow_app.py

In MAC:
export FLASK_APP=starter_app.py

# How to run the app

flask run
or
python app.py

# With reloader

flask --app calmcrow_app.py --debug run

# Generate requirements

pip freeze > requirements.txt
