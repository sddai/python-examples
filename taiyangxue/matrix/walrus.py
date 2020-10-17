# 海象操作符

a = [1,2,3,4,5]
if n := len(n) > 4:
    print(n)

# 命令行中执行
a = "wtf_walrus"
a := "wtf_walrus"  # 报错！
(a := "wtf_walrus") # 奇迹发生，竟然通过了！

a = 6, 9  # 元组赋值

(a := 6, 9)  # 海象赋值，表达式结果正常
# 现在 a 的值是多少？

a, b = 6, 9 # 解包赋值
(a, b = 16, 19) # Oh no！

(a, b := 16, 19) # 这里竟然打印出三员元组！

# 现在的 a 是多少？