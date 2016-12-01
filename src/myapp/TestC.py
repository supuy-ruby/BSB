# -*- coding: utf-8 -*-
from myapp import app,res,req
import json

@app.route('/getdata/', methods=['POST','GET'])
def getdata():
    result=[{'url':'images/baobiao_09.png','name':u'进销存报表'},{'url':'images/baobiao_05.png','name':u'网格类报表'},{'url':'images/baobiao_03.png','name':u'收入类报表'},
            {'url':'images/baobiao_10.png','name':u'损益类报表'},{'url':'images/baobiao_09.png','name':u'进销存报表'},{'url':'images/baobiao_05.png','name':u'网格类报表'},{'url':'images/baobiao_03.png','name':u'收入类报表'},
            {'url':'images/baobiao_10.png','name':u'损益类报表'}]
    jsonData = json.dumps(result)
    resp = res(jsonData)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp