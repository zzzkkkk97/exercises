#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    # 1. connect to info.db
    con = sqlite3.connect("info.db")
    # 2. select * from students
    data = list(con.execute("select * from students"))
    # 3. render_template
    return render_template("index.html", data=data)
