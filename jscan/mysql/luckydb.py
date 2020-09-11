import pymysql


def connect():
    db = pymysql.connect("192.168.119.136", "lucky", "lucky", "lucky")
    return db


def t_query_by_SQL(sql):
    """get term"""
    db = connect()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as e:
        print(e.args)
    cursor.close()
    db.close()
    return result
