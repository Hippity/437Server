# 437Server
# AUBitcoinServer
Server for the AUBitcoin project

**#Step 1**

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

set FLASK_APP=app.py

set FLASK_ENV=development

flask run

**Wont work yet**

**#Step 2**

Create a new schema on MySQL Workbench named aubitcoin, that will store all the data needed for our application.

Create db_config.py file and this line

DB_CONFIG = 'mysql+pymysql://<**mysql_username**>:<**mysql_password**>@<**mysql_host**>:<**mysql_port**>/<**mysql_db_name**>'

change whats in bold

**Example:**

DB_CONFIG = "mysql+pymysql://root:QWERTY1965asdf@127.0.0.1:3306/aubitcoin"


**#Step 3**

On the terminal 

python

from app import db

db.create_all()

exit()

**This should create the needed tables in your database**
