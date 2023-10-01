echo "BUILD START"
Python 3.7.0 -m pip install -r requirements.txt



# Collect static files
Python 3.7.0 manage.py collectstatic --noinput --clear

echo "BUILD END"