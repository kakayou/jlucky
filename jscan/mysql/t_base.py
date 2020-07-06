import pymysql
import mysql.luckydb as db

def t_base_insert(args=None):
    """初始化t_base"""
    if args is None:
        args = ()
    con = db.connect()
    cursor = con.cursor()
    sql = "INSERT INTO t_base (red1, red2, red3, red4, red5, red6, blue) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', " \
          "'%s') "
    try:
        cursor.executemany(sql, args)
        con.commit()
    except:
        con.rollback()
    cursor.close()
    con.close()
    return

def t_base_clear(args=None):
    """初始化t_base"""
    if args is None:
        args = ()
    con = db.connect()
    cursor = con.cursor()
    sql = "DELETE FROM t_base"
    try:
        cursor.execute(sql, args)
        con.commit()
    except:
        con.rollback()
    cursor.close()
    con.close()
    return