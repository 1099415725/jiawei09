# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/26   16:21
# 开发工具： PyCharm



from flask import Flask
app=Flask(__name__)
resp_dic={"code":200,"data":{"customerNum":2342,"contactsNum":0,"businessNum":0,"contractNum":0,"recordNum":4000,"receivablesNum":0,"businessStatusNum":0},"error":""}
@app.route("/")
def hello():
    return resp_dic

if __name__=="__main__":
    app.run()