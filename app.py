"""
simple python flask application
"""

##########################################################################
## Imports
##########################################################################

import os
import pandas as pd
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask.json import jsonify
import classfy
import pickle
import random
import json
##########################################################################
## Model load & data
##########################################################################


##########################################################################
## Application Setup
##########################################################################

app = Flask(__name__)

##########################################################################
## Routes
##########################################################################

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/hello")
def hello():
    """
    Return a hello message
    """
    return jsonify({"hello": "world"})

@app.route("/api/hello/<name>")
def hello_name(name):
    """
    Return a hello message with name
    """
    return jsonify({"hello": name})

@app.route("/api/whoami")
def whoami():
    """
    Return a JSON object with the name, ip, and user agent
    """
    return jsonify(
        name=request.remote_addr,
        ip=request.remote_addr,
        useragent=request.user_agent.string
    )

@app.route("/api/whoami/<name>")
def whoami_name(name):
    """
    Return a JSON object with the name, ip, and user agent
    """
    return jsonify(
        name=name,
        ip=request.remote_addr,
        useragent=request.user_agent.string
    )
@app.route("/api/classify")
def classify():
    """
    Return a result message
    """
    loaded_model = pickle.load(open('save/neigh.sav', 'rb'))
    test = pd.read_csv('mlflowe/fashion-mnist_test.csv')
    X_test = test.iloc[:,1:]
    y_test = test['label']
    score = loaded_model.score(X_test, y_test)
    print(score)
    num = random.randint(0,len(test))
    y_prd = loaded_model.predict(X_test[num-1:num])
    str()
    resualt = {"score":score,"y_prd":y_prd,"Y_real":y_test[num]}
    json_str = json.dumps({'name': 'Alice', 'age': 30})
    return jsonify({"resualt": str(y_prd[0]),
                    "score": str(score),
                    "Y_real":str(y_test[num])})
##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
    app.run()
