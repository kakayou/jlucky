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


def t_facility():
    """get t_facility"""
    con = db.connect()
    cursor = con.cursor()
    sql = "SELECT red1, red2, red3, red4, red5, red6, blue FROM t_facility ORDER by term desc"
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
        new.append((int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]), int(x[6])))
    return new

def t_facility_Reds():
    """get t_facility"""
    con = db.connect()
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
    con = db.connect()
    cursor = con.cursor()
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
    con = db.connect()
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


def t_facility_row_sum():
    """get term"""
    con = db.connect()
    cursor = con.cursor()
    sql = "select COUNT(*) as v_count,tf.v_value from (select red1+red2+red3+red4+red5+red6+blue as v_value from t_facility) tf GROUP BY tf.v_value order by v_count DESC"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as e:
        print(e.args)
    cursor.close()
    con.close()
    return result


def t_facility_sql(sql):
    """get term"""
    con = db.connect()
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as e:
        print(e.args)
    cursor.close()
    con.close()
    return result


def t_facility_odd():
    """get odd count"""
    con = db.connect()
    cursor = con.cursor()
    odd_dict = {}
    try:
        cursor.execute("SELECT red1, red2, red3, red4, red5, red6, blue FROM t_facility ORDER by term desc")
        data = cursor.fetchall()
        odd_dict = {}
        for item in data:
            result = 0
            for i in range(len(item)):
                if int(str(item[i])) % 2 == 0:
                    result = result + 1
            if result in odd_dict.keys():
                v_count = odd_dict[result] + 1
                odd_dict[result] = v_count
            else:
                odd_dict[result] = 1
    except Exception as e:
        print(e.args)
    cursor.close()
    con.close()
    sortedList = sorted(odd_dict.items(), key=lambda d: d[1], reverse=True)
    odd_dict.clear()
    for item in sortedList:
        odd_dict[item[0]] = item[1]
    return odd_dict
