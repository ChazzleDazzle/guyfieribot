#!/usr/bin/env python3

from sqlalchemy import create_engine

db_connect = create_engine("sqlite:///flavortown.db")


def write_menu_item(title, description):
    conn = db_connect.connect()
    query = conn.execute(
        f"INSERT INTO menu (title, description) VALUES ({title}, {description});"
    )
