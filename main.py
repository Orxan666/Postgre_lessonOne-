import psycopg2
connection = psycopg2.connect(
    user='postgres',
    password='Orxan_666',
    host='localhost',
    port='5432',
    database='movie'
) 

cursor =connection.cursor()

query="""
CREATE TABLE film_site(
id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL,
description TEXT NOT NULL,
view INT NOT NULL DEFAULT 0,
janrId  UNIQUE NOT NULL,
release_date DATE,
has_fragman BOOLEAN true NOT NULL


),
CREATE TABLE store{
    id SERAIL PRIMARY KEY,
    name VARCHAR(50) NOT NULL ,
    count INT NOT NULL DEFAULT 0,
    is_news BOOLEN true NOT NULL,
    saticiId  INT NOT NULL,
    release_date DATE ,
    release_time TIME,
    last TIME,
    price int NOT NULL ,
    sale_count int DEFAULT 0,
    bar_code INT NOT NULL UNIQUE



}
"""

cursor.execute(query)
connection.commit()