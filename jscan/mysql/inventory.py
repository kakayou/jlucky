# _*_coding:utf-8_*_
# =========================================================================
"""
-- File Name : inventory.py
-- Purpose : 从mysql数据中动态获取主机列表，动态inventory,不用维护主机列表
-- Author:刘骥
"""
# =========================================================================
import pymysql
import json
import sys


def execude_sql(name):  # 定义一个执行SQL的函数
    sql = 'select name,ip,port,username,password from t_assets where name="{0}";'.format(name)
    cur.execute(sql)  # args即要传入SQL的参数
    sys_result = cur.fetchall()
    hostlist = {}  # empty dict
    for i in sys_result:
        hostlist[i[0]] = []
    for i in sys_result:
        hostlist[i[0]].append([i[1], i[2], i[3], i[4]])
    host_lists = dict()
    for i in hostlist.items():
        dict_item = dict()
        for index in i[1]:
            dict_item[index[0]] = {'ansible_connection': 'ssh', 'ansible_ssh_port': index[1], 'ansible_ssh_user': index[2], 'ansible_ssh_pass': index[3]}
        host_lists[i[0]] = dict_item
    print(host_lists)
    return host_lists


def group(data):
    '''
    all hostip
    :param data:
    :return:
    '''
    count_ip = dict()
    count_ip['all'] = {}
    count_ip['all']['hosts'] = []
    index = []
    for i in data:
        index.extend(data[i].keys())
    count_ip['all']['hosts'].extend(list(set(index)))
    print
    json.dumps(count_ip, indent=4)


if __name__ == "__main__":
    global file, con, cur  # 文件对象，连接和游标对象
    # 连接数据库
    con = pymysql.connect('66.1.1.133', 'devops', 'devops', 'devops', charset='utf8')  # 连接数据库
    cur = con.cursor()  # 定义一个游标
    group_name = sys.argv[2]
    data = execude_sql(group_name)
    if sys.argv[1] == '--list':
        group(data)
    else:
        print
        "Usage %s --list or --host <hostname>" % sys.argv[0]
        sys.exit(1)
