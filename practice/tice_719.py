# encoding:utf-8
# 开发团队：SDET_05
# 开发人员：渣渣灰
# 开发时间： 2019/7/19   10:22
# 文件名称： tice_719.py
# 开发工具： PyCharm
# while True:
#     age1=int(input("输入男的年龄："))
#     age2=int(input("输入女的年龄："))
#     try:
#         age1
#         age2
#     except:
#         print("输入的年龄有误，重新输入！")
#     else:
#         print("真听话")
#     finally:
#         print("结束")
# try:
#     mem=input("请输入联系人姓名：\n")
#     tel=int(input("请输入联系人电话：\n"))
#     len(tel)==11
#     0<len(mem)<20
# except:
#     print("输入有误！")
# dict={}
# dict[tel]=mem
# print(dict)
# ser_tel=input("请输入要查找的联系人电话:\n")
# for key in dict.keys():
#     if ser_tel==key:
#         val=dict[key]
#         print(val,  ser_tel)
#
# del_mem=input("请输入要删除的联系人：\n")


def devision():
    num1 = int(input("请输入除数："))
    num2 = int(input("请输入被除数："))

    # 使用 assert 断言语句
    assert num2 != 0, "除数不可为0"
    result = num1 / num2
    return result

while True:
    if __name__ == "__main__":
        cc=devision()
        try:
            print( devision() ) # 调用函数
        except AssertionError as e:
            print("\n输入有误",e)  # 处理AssertionError异常

