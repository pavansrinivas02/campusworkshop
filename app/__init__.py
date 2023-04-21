"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="postgres://root:dpg-ch12vrorddl13a53qaig-a.oregon-postgres.render.com",
        database="mytodo_x17e",
        user="root",
        password="Ewh6KcJLOSqvyroQxbLtrvYdFcDLxOHt")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
