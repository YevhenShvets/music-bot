from src.db.connect import *
from .select import select_film_activity, select_music_activity
from .insert import insert_film_activity, insert_music_activity


def update_film_activity(film_id):
    film_activity = select_film_activity(film_id)
    if film_activity:
        cur = conn.cursor()
        cur.execute('UPDATE "FilmActivity" SET count_get=%s WHERE film_id=%s;',
                    ((film_activity['count_get']+1), film_id))
        conn.commit()
        cur.close()
    else:
        insert_film_activity(film_id)


def update_music_activity(music_id):
    music_activity = select_music_activity(music_id)
    if music_activity:
        cur = conn.cursor()
        cur.execute('UPDATE "MusicActivity" SET count_get=%s WHERE music_id=%s;',
                    ((music_activity['count_get'] + 1), music_id))
        conn.commit()
        cur.close()
    else:
        insert_music_activity(music_id)
