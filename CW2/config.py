
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configure data
app.config['SQLALCHEMY_DATABASE_URI'] = (
    "mssql+pyodbc:///?odbc_connect="
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=dist-6-505.uopnet.plymouth.ac.uk;"
    "DATABASE=COMP2001_JOsborneWalker;"
    "UID=JOsborneWalker;"
    "PWD=SpqD287*;"
    "TrustServerCertificate=yes;"
    "Encrypt=yes;"
)

# enable tracking modifications 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
