#!/usr/bin/env python3

from sqlalchemy import create_engine
import bs4, requests

db_connect = create_engine("sqlite:///flavortown.db")

def scrape_flavor():
    r = requests.get('http://highwaytotheflavorzone.com')
    r.raise_for_status()
    flavor = bs4.BeautifulSoup(r.text, features='html.parser')
    t = flavor.h1.contents
    d = flavor.h2.contents
    return t, d

def write_menu_item(title, description):
    conn = db_connect.connect()
    query = conn.execute(
        f'INSERT INTO menu (title, description) VALUES ("{title}", "{description}");'
    )

# title = scrape_flavor()[0]
# description = scrape_flavor()[1]

for i in range (0, 500):
    title = scrape_flavor()[0][0]
    description = scrape_flavor()[1][0]
    print(title, description)
    write_menu_item(title, description)
    i = i + 1
    
