# -*- coding: utf-8 -*-
from myapp import app,res,req,urlfor,render_template,make_response
import json
import time
@app.route('/login', methods=['POST'])
def login():
    user={
      "uid": "",
      "username": "",
      "name": "",
      "reg_time": "",
      "last_login_time": "",
    }
    result = {
        "error_code": 0,
        "data":None
    }
    username=req.form['username']
    userpass=req.form['userpass']
    #读取数据库找到是否有用户
    jsonData = json.dumps(result)
    print username
    resp=res(jsonData)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/<index>-<int:index1>',methods=['post','get'])
def index(index,index1):
    serachCode=req.args.get('key','')
    return render_template('index.html',name=serachCode)

@app.route('/cookie')
def cookie():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('username', 'the username')
    return resp


with app.test_request_context():
    pass
    print urlfor('index',index='index',index1='1')
    #print urlfor('login')
    #print urlfor('login', next='/')
    #print urlfor('profile', username='John Doe')

#解析json
def jiexiJSON(text):
    dataJsonStr = text.replace("\\r\\n", "")
    return json.loads(dataJsonStr)




