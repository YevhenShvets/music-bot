from .connect import *


def select_film(id: int):
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


async def select_films_name():
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


def select_music(music_id):
    cur = conn.cursor()
    cur.execute('SELECT id, name, author, url FROM "Music" WHERE id=%s', (music_id,))

    music_list = cur.fetchall()

    musics = []
    for row in music_list:
        r = {
            "id": row[0],
            "name": row[1],
            "author": row[2],
            "url": row[3],
        }
        musics.append(r)
    return musics[0]


def select_music_list(film_id):
    cur = conn.cursor()
    cur.execute('SELECT "Music".id, "Music".name, "Music".author, "Music".url FROM "Music" INNER JOIN "Film_Music" '
                'ON "Film_Music".music_id ="Music".id WHERE "Film_Music".film_id = %s', (film_id, ))

    music_list = cur.fetchall()

    musics = []
    for row in music_list:
        r = {
            "id": row[0],
            "name": row[1],
            "author": row[2],
            "url": row[3]
        }
        musics.append(r)
    return musics


def select_liked_music(user_id):
    cur = conn.cursor()
    cur.execute('SELECT "Music".id, "Music".name, "Music".author, "Music".url FROM "Music" INNER JOIN "LikedMusic" '
                'ON "LikedMusic".music_id ="Music".id WHERE "LikedMusic".user_id = %s', (user_id, ))

    music_list = cur.fetchall()

    musics = []
    for row in music_list:
        r = {
            "id": row[0],
            "name": row[1],
            "author": row[2],
            "url": row[3]
        }
        musics.append(r)
    return musics

