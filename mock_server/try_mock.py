# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/28   12:21
# 开发工具： PyCharm


from flask import Flask,request
app=Flask(__name__)


resp_today={"code":200,"data":{"customerNum":100,"contactsNum":10015,"businessNum":2210,"contractNum":0,"recordNum":0,"receivablesNum":0,"businessStatusNum":0},"error":""}
resp_yesterday={"code":200,"data":{"customerNum":90,"contactsNum":10000,"businessNum":2200,"contractNum":0,"recordNum":0,"receivablesNum":0,"businessStatusNum":0},"error":""}

@app.route("/",methods=["GET","POST"])
def say_hello():
    req_type=str(request.data).split('"')[3]
    if req_type=="today":
        return resp_today
    elif req_type=="yesterday":
        return resp_yesterday

if __name__=='__main__':
    app.run()