#账户管理系统  UTF-8  coding by HYJ
'''
#主程序
print("#####欢迎使用账户管理系统！#####")
print("请输入序号:")
print("1.注册账户")
print("2.登录账户")
print("3.退出系统")
key1 = int(input("请输入序号："))
if key1 == 1:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    print("正在注册账户...")
    print("注册成功！")
    print("username:",username)
    print("password:******")
if key1 == 2:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    print("正在登录账户...")
    print("登录成功！")
    print("username:",username)
    print("password:******")
if key1 == 3:
    print("正在退出系统...")
    print("退出成功！")
if key1 != 1 and key1 != 2 and key1 != 3:
    print("输入错误，请重新输入！")
    '''



# 账户管理系统（使用字典存储） UTF-8  coding by HYJ

# 用字典存储账户：用户名 -> 密码
users = {}   # 复习：字典

# 用一个列表存储操作日志（复习列表和切片）
log = []
#标记变量
flag = False
# 主循环
while True:
    print("\n##### 欢迎使用账户管理系统！#####")
    print("1. 注册账户")
    print("2. 登录账户")
    print("3. 查看所有用户名")
    print("4. 退出系统")
    print("5.删除用户")
    key1 = input("请输入序号：")
    key1 = int(key1)
    if key1!=1 and key1!=2 and key1!=3 and key1!=4 and key1!=5:
        print("输入错误，请输入数字！")
        continue
    

    if key1 == 1:
        username = input("请输入用户名：")
        if username in users:
            print("用户名已存在！")
            continue
        password = input("请输入密码：")
        users[username] = password
        log.append(f"注册: {username}")   # 列表追加
        print("注册成功！")
        print("username:",username)
        print("password:******")

    elif key1 == 2:
        username = input("请输入用户名：")
        password = input("请输入密码：")
        if username in users and users[username] == password:
            print("登录成功！")
            flag = True
            log.append(f"登录: {username}")
        else:
            print("用户名或密码错误！")

    elif key1 == 3:
        # 复习：将字典的键转换成列表，再切片显示
        name_list = list(users.keys())   # 得到所有用户名列表
        if not name_list:
            print("暂无注册用户")
        else:
            # 用元组打包显示 (索引, 用户名)  复习元组
            for idx, name in enumerate(name_list):
                t = (idx+1, name)        # 元组
                print(f"{t[0]}. {t[1]}")
            # 复习切片：显示前3个用户
            print("\n前3个用户:", name_list[:3])
            # 复习切片步长：显示奇数位置的用户
            print("奇数位置用户:", name_list[::2])

    elif key1 == 4:
        # 退出前显示操作日志（最后5条）
        print("\n===== 本次操作日志（最后5条） =====")
        # 复习列表切片：取最后5个元素
        for entry in log[-5:]:
            print(entry)
        print("正在退出系统...")
        break
    elif key1 == 5:
        username = input("请输入要删除的用户名:")
        if username in users and flag == True:
            del users[username]
            log.append(f"删除: {username}")
            print("用户删除成功！")
        else:
            print("请检查用户名是否正确或您是否有权限删除！")
    else:
        print("输入错误，请重新输入！")