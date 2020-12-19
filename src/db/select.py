from .connect import *


def get_film(id: int):
    cur = conn.cursor()
    cur.execute('SELECT id, name, type, description, director, image_url FROM "Film" WHERE id=%s;', (id,))

    films_list = cur.fetchall()

    films = []
    for row in films_list:
        r = {
            "id": row[0],
            "name": row[1],
            "type": row[2],
            "description": row[3],
            "director": row[4],
            "image_url": row[5]
        }
        films.append(r)
    return films[0]


async def get_films_name():
    cur = conn.cursor()
    cur.execute('SELECT id, name FROM "Film";')

    films_list = cur.fetchall()

    films = []
    for row in films_list:
        r = {
            "id": row[0],
            "name": row[1]
        }
        films.append(r)
    return films

