import pymysql

mysql_ip="192.168.119.136"

def connect():
    db = pymysql.connect(mysql_ip, "lucky", "lucky", "lucky")
    return db


def t_facility_insert(args=None):
    """更新t_facility"""
    if args is None:
        args = ()
    db = pymysql.connect(mysql_ip, "lucky", "lucky", "lucky")
    cursor = db.cursor()
    sql = "INSERT INTO t_facility (term, red1, red2, red3, red4, red5, red6, blue) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
    try:
        cursor.executemany(sql, args)
        db.commit()
    except  Exception as e:
        print(e.args)
        db.rollback()
    cursor.close()
    db.close()
    return

def t_query_by_SQL(sql):
    """get term"""
    db = pymysql.connect(mysql_ip, "lucky", "lucky", "lucky")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except  Exception as e:
        print(e.args)
    cursor.close()
    db.close()
    return result
