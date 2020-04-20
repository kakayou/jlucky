import pymysql

mysql_ip="192.168.119.137"

def t_base_insert(args=None):
    """初始化t_base"""
    if args is None:
        args = ()
    db = pymysql.connect(mysql_ip, "lucky", "lucky", "lucky")
    cursor = db.cursor()
    sql = "INSERT INTO t_base (red1, red2, red3, red4, red5, red6, blue) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', " \
          "'%s') "
    try:
        cursor.executemany(sql, args)
        db.commit()
    except:
        db.rollback()
    cursor.close()
    db.close()
    return


def t_facility_insert(args=None):
    """更新t_facility"""
    if args is None:
        args = ()
    db = pymysql.connect(mysql_ip, "lucky", "lucky", "lucky")
    cursor = db.cursor()
    sql = "INSERT INTO t_facility (term, red1, red2, red3, red4, red5, red6, blue) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') "
    try:
        cursor.executemany(sql, args)
        db.commit()
    except  Exception as e:
        print(e.args)
        db.rollback()
    cursor.close()
    db.close()
    return


def t_facility_max_term():
    """get t_facility"""
    db = pymysql.connect(mysql_ip, "lucky", "lucky", "lucky")
    cursor = db.cursor()
    sql = "SELECT MAX(term) FROM t_facility"
    maxTerm = ""
    try:
        cursor.execute(sql)
        maxTerm = cursor.fetchone()
    except  Exception as e:
        print(e.args)
    cursor.close()
    db.close()
    return maxTerm

def t_facility_reds():
    """get t_facility"""
    db = pymysql.connect(mysql_ip, "lucky", "lucky", "lucky")
    cursor = db.cursor()
    sql = "SELECT red1, red2, red3, red4, red5, red6 FROM t_facility"
    result = ()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except  Exception as e:
        print(e.args)
    cursor.close()
    db.close()
    new = list()
    for x in result:
        new.append((int(x[0]),int(x[1]),int(x[2]),int(x[3]),int(x[4]),int(x[5])))
    return new

def t_facility_group_term():
    "get term"
    db = pymysql.connect(mysql_ip, "lucky", "lucky", "lucky")
    cursor = db.cursor()
    sql = "select count(*) as termCount,blue from t_facility GROUP BY blue ORDER by termCount desc"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except  Exception as e:
        print(e.args)
    cursor.close()
    db.close()
    return result


def t_query_by_SQL(sql):
    "get term"
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
