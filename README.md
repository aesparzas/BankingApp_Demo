# BankingApp
Banking App demonstrating some Django Features that can handle balance and transferences between users
## Running the App
To run the app you need a working database called banking_database on MySql
 and a python enviroment using django and other needed packages. All the
 requirements are in etc/requirements.txt file. So use
```
python -m venv tmp/venv
. venv/bin/activate
pip install -r etc/requirements.txt
```
And you are ready to go.
Run the server using 
```
cd src
./manage.py runserver
```

## Built with
* [Django](https://www.djangoproject.com/) - The web framework used
* [MySQL](https://www.mysql.com/) - Relational DBMS
## Authors
* **Adolfo Esparza** - *Initial work* - [aesparzas](https://github.com/aesparzas)
