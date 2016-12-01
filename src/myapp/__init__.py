from flask import Flask,request,Response, url_for,render_template,make_response
app = Flask(__name__)
req=request
res=Response
urlfor=url_for
import  myapp.Member
import  myapp.TestC