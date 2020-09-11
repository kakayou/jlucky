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

def t_sums():
    """get t_facility"""
    con = pymysql.connect()
    cursor = con.cursor()
    sql = "SELECT v_count, v_sum FROM t_sum ORDER by v_count desc"
    result = ()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as e:
        print(e.args)
    cursor.close()
    con.close()
    new = list()
    for x in result:
        new.append((int(x[0]), int(x[1])))
    return new