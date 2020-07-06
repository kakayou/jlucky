import pymysql
import mysql.luckydb as db

def t_facility_max_term():
    """get t_facility"""
    con = db.connect()
    cursor = con.cursor()
    sql = "SELECT MAX(term) FROM t_facility"
    maxTerm = ""
    try:
        cursor.execute(sql)
        maxTerm = cursor.fetchone()
    except  Exception as e:
        print(e.args)
    cursor.close()
    con.close()
    return maxTerm

def t_facility_reds():
    """get t_facility"""
    con = pymysql.connect()
    cursor = con.cursor()
    sql = "SELECT red1, red2, red3, red4, red5, red6 FROM t_facility ORDER by term desc"
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
        new.append((int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5])))
    return new

def t_facility_group_term():
    """get term"""
    con = pymysql.connect()
    cursor = db.cursor()
    sql = "select count(*) as termCount,blue from t_facility GROUP BY blue ORDER by termCount desc"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as e:
        print(e.args)
    cursor.close()
    con.close()
    return result

def t_facility_insert(args=None):
    """更新t_facility"""
    if args is None:
        args = ()
    con = pymysql.connect()
    cursor = con.cursor()
    sql = "INSERT INTO t_facility (term, red1, red2, red3, red4, red5, red6, blue) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
    try:
        cursor.executemany(sql, args)
        con.commit()
    except  Exception as e:
        print(e.args)
        con.rollback()
    cursor.close()
    con.close()
    return