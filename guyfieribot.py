#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import slack
import requests
from pyquery import PyQuery


db_connect = create_engine("sqlite:///flavortown.db")
app = Flask(__name__)
api = Api(app)


class Menu(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute(
            "SELECT title, description FROM menu ORDER BY RANDOM() LIMIT 1;"
        )
        message = query.cursor.fetchone()
        return {"title": message[0], "description": message[1]}


api.add_resource(Menu, "/flavortown")


if __name__ == "__main__":
    app.run(port="5002")
