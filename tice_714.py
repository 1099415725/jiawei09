# encoding:utf-8


# result=0
# for i in range(1,101):
#     act_result=result+i
#     print(act_result)

#
# for num in range(1,7):
#     print("这是第",num,"行",end=":")
#     for card in range(1,7):
#         print(card,end=",")
#     print("")

# 任务1，输出字母或数字的ASCII值
# while True:
#     num = input("你的输入值：\n")
#     if ord("A") <= ord(num) <= ord("Z") or ord("a") <= ord(num) <= ord("z") or ord("0") <= ord(num) <= ord("9"):
#         print(num, "的ASCII值是：", ord(num))
#     else:
#         print("退出成功！")
#         break

# 任务2：编程输出星号（*）阵列
# star = 0
# for num in range(1, 21):
#     star += 1
#     new_star = star * "*"
#     print(new_star)

# 任务3：求1到5的阶乘的和
# num = int(input("输入你要求的阶乘数：\n"))




# 任务4：打印九九乘法表

# for num2 in range(1, 10):
#     print(" ")
#     for i in range(1, num2 + 1):
#         num3 = num2 * i
#         print(num2, "*", i, "=", num3, end="   ")
# print("")

# 任务5 打印所有的水仙花数
# for num1 in range(1, 10):
#     for num2 in range(0, 10):
#         for num3 in range(0, 10):
#             num4 = num1 * 100 + num2 * 10 + num3
#             num5 = num1 ** 3 + num2 ** 3 + num3 ** 3
#             if num4 == num5:
#                 print(num4)

# 任务6：猴子吃桃子问题
peach_list=[1,]
for i in range(1,10):
    new_peach=(int(peach_list[-1])+1)*2
    peach_list.append(new_peach)
print(peach_list)
print(peach_list[-1])
