import pymysql
import mysql.luckydb as db

def t_sum_insert(args=None):
    """初始化t_base"""
    if args is None:
        args = ()
    con = db.connect()
    cursor = con.cursor()
    sql = "INSERT INTO t_sum (v_count, v_sum) VALUES (%s, %s)"
    try:
        cursor.executemany(sql, args)
        con.commit()
    except:
        con.rollback()
    cursor.close()
    con.close()
    return

def t_sum_clear():
    """初始化t_sum"""
    con = db.connect()
    cursor = con.cursor()
    sql = "DELETE FROM t_sum"
    try:
        cursor.execute(sql)
        con.commit()
    except:
        con.rollback()
    cursor.close()
    con.close()
    return