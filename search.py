# -*- coding: UTF-8 -*-
import sqlite3
import pprint

def sqlite_read():
    """python读取sqlite数据库文件
    """
    mydb = sqlite3.connect('datafile.db')       # 链接数据库
    cur = mydb.cursor()                         # 创建游标cur来执行SQL语句

    # 获取表名
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    Tables = cur.fetchall()                     # Tables 为元组列表
    # print(Tables)
    language = []
    for i in range(len(Tables)):
        language.append(Tables[i][0])
    # print(language)
    return language
# sqlite_read()