#!/usr/bin/env python3

from sqlalchemy import create_engine
import bs4, requests

db_connect = create_engine("sqlite:///flavortown.db")

def scrape_flavor():
    r = requests.get('http://highwaytotheflavorzone.com')
    r.raise_for_status()
    flavor = bs4.BeautifulSoup(r.text, features='html.parser')
    title = flavor.h1.contents
    description = flavor.h2.contents
    return title, description

def write_menu_item(title, description):
    conn = db_connect.connect()
    query = conn.execute(
        f"INSERT INTO menu (title, description) VALUES ({title}, {description});"
    )
