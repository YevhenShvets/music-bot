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
    cur.close()
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
    cur.close()
    return films


async def select_top_films_name():
    cur = conn.cursor()
    cur.execute('SELECT id, name FROM "Film" INNER JOIN "FilmActivity" ON "FilmActivity".film_id="Film".id '
                'ORDER BY "FilmActivity".count_get DESC;')

    films_list = cur.fetchall()

    films = []
    for row in films_list:
        r = {
            "id": row[0],
            "name": row[1]
        }
        films.append(r)
    cur.close()
    return films


async def select_search_films_name(search_film):
    cur = conn.cursor()
    cur.execute('SELECT id, name FROM "Film" WHERE name iLIKE ' + "'%" + search_film + "%';")

    films_list = cur.fetchall()

    films = []
    for row in films_list:
        r = {
            "id": row[0],
            "name": row[1]
        }
        films.append(r)
    cur.close()
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
    cur.close()
    return musics[0]


def select_top_music():
    cur = conn.cursor()
    cur.execute('SELECT id, name, author, url FROM "Music" INNER JOIN "MusicActivity" '
                'ON "MusicActivity".music_id="Music".id ORDER BY "MusicActivity".count_get DESC;')

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
    cur.close()
    return musics


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
    cur.close()
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
    cur.close()
    return musics


def select_film_activity(film_id):
    cur = conn.cursor()
    cur.execute('SELECT film_id, count_get FROM "FilmActivity" WHERE film_id=%s;', (film_id,))
    activity = cur.fetchall()
    r = {}
    for row in activity:
        r['film_id'] = row[0]
        r['count_get'] = row[1]
    cur.close()
    return r


def select_music_activity(music_id):
    cur = conn.cursor()
    cur.execute('SELECT music_id, count_get FROM "MusicActivity" WHERE music_id=%s;', (music_id,))
    activity = cur.fetchall()
    r = {}
    for row in activity:
        r['music_id'] = row[0]
        r['count_get'] = row[1]
    cur.close()
    return r

