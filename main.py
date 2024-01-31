from flask import Flask, render_template, url_for, request
from modulePython.UT_SQL import *
import sqlite3
import datetime
from os import system

system("pip install flask")
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/name.html')
def nameTournament():
    return render_template("name.html")

@app.route('/createTournament', methods=["GET"])
def createTournament():
    result=request.args.get("tournamentName")
    date = datetime.datetime.now()
    #create the SQL request
    with open("BDD/bdd_template",'r') as file:
        createSQL = file.read()
    #create the database, connect and execute the request
    conn = connect("BDD/"+result.replace(" ", "_").replace("-", "_").replace("/", "_")+ "_" + str(date.year) +"_" + str(date.month) + "_" + str(date.day) + "_" + str(date.hour) + "_" + str(date.minute) + "_" + str(date.second))
    conn.isolation_level = None
    curs = conn.cursor()
    curs.executescript(createSQL)
    curs.close()
    return render_template("name.html")

app.run(host="localhost", port="8000")