# -*- coding: utf-8 -*-
import psycopg2
import gl
class pyhelper:
# 数据库连接参数
    conn = psycopg2.connect(database="TSTStore", user=gl.pguid, password=gl.pgpwd, host=gl.pghost, port=gl.pgport)
    cur = conn.cursor()
    cur.execute('SELECT * FROM "Members";')
    rows = cur.fetchall()  # all rows in table
    print(rows)
    for i in rows:
        print(i)
    conn.commit()
    cur.close()
    conn.close()

