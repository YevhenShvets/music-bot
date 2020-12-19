from .connect import *


def insert_user(user_id, fullname_user):
    """
    Add user info to db
    :param user_id: from_user.id
    :param fullname_user: from_user.fullname
    :return: None
    """
    cur = conn.cursor()
    cur.execute('INSERT INTO "User"(telegram_id, fullname) VALUES(%s, %s) '
                'ON CONFLICT (telegram_id) DO UPDATE SET fullname=%s;', (user_id, fullname_user, fullname_user))
    conn.commit()
    insert_user_settings(user_id, "Uk", 5)
    cur.close()


def insert_user_settings(user_id, language, list_count):
    """
    Create user settings
    :param user_id: from_user.id
    :param language: Uk
    :param list_count: 5
    :return:
    """
    cur = conn.cursor()
    cur.execute('INSERT INTO "UserSettings"(user_id, language, list_count) VALUES(%s, %s, %s)'
                'ON CONFLICT(user_id) DO UPDATE SET language=%s, list_count=%s',
                (user_id, language, list_count, language, list_count))
    conn.commit()
    cur.close()
