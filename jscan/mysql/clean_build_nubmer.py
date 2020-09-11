import pymysql

db = pymysql.connect("66.1.1.133", "devops", "devops", "devops")
cursor = db.cursor()
try:
    cursor.execute("select name from t_task")
    result = cursor.fetchall()
    print(len(result))

    for task in result:
        sql ='''SELECT ts.build_number FROM t_task_script ts LEFT JOIN t_task t ON t.id=ts.ref_task_id WHERE 1=1 AND t.name = "{0}" GROUP BY ts.build_number HAVING COUNT(*)>1'''.format(task[0])
        print(task[0])
        cursor.execute(sql)
        builder_numbers = cursor.fetchall()
        print(len(builder_numbers))
        if len(builder_numbers) > 0:
            for num in builder_numbers:
                print(num[0])
                sql_ids='''SELECT ts.id FROM t_task_script ts LEFT JOIN t_task t ON t.id=ts.ref_task_id WHERE 1=1 AND t.name = "{0}" AND ts.build_number={1} order by ts.create_time desc'''.format(task[0], num[0])
                cursor.execute(sql_ids)
                ids = cursor.fetchall()
                for n in range(len(ids)):
                    if n > 0:
                       d_sql="DELETE FROM t_task_script where id='{0}'".format(ids[n][0])
                       print(d_sql)
                       cursor.execute(d_sql)
                       db.commit()
except Exception as e:
    print(e.args)