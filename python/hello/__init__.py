#!/usr/bin/env python3

from flask import Flask, Response, json

app = Flask(__name__)

@app.route("/")
def hello():
    return Response(json.dumps({'text' : 'Hello world'}))
