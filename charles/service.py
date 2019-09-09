# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/8/20   10:43
# 开发工具： PyCharm

from flask import Flask,request

app = Flask(__name__)
ret_dic_today={"code":200,"data":{"customerNum":9090,"contactsNum":1290,"businessNum":666,"contractNum":24543,"recordNum":66,"receivablesNum":0,"businessStatusNum":0},"error":""}
ret_dic_yesterday={"code":200,"data":{"customerNum":9000,"contactsNum":1200,"businessNum":666,"contractNum":24543,"recordNum":66,"receivablesNum":0,"businessStatusNum":0},"error":""}
ret_dic_week={"code":200,"data":{"customerNum":8600,"contactsNum":1100,"businessNum":666,"contractNum":24543,"recordNum":66,"receivablesNum":0,"businessStatusNum":0},"error":""}

@app.route("/",methods=['GET','POST'])
def hello():
    ret_type=str(request.data).split("\"")[3]
    if ret_type=="today":
        return ret_dic_today
    elif ret_type=="yesterday":
        return ret_dic_yesterday
    elif ret_type=="week":
        return ret_dic_week
    else:
        return


    # print(type(ret_type))
    # print (ret_type)
    # return ret_dic



if __name__=='__main__':
    app.run()