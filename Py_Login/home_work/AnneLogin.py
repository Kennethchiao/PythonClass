import os, ast

def display():
    print("====================")
    print("1. 創建帳號密碼")
    print("2. 顯示帳號密碼")
    print("3. 修改帳號密碼")
    print("4. 刪除帳號密碼")
    print("其他任意鍵結束")
    print("====================")

def create():
    while True:
        account = input("請輸入帳號：")
        if account in data:
            print("帳號已存在")
        else:
            password = input("請輸入密碼：")
            data[account] = password
            with open(file_name, 'w') as file:
                file.write(str(data))
            break

def show():
    keys = data.keys()
    print("\n/* 所有帳號密碼如下 */")
    print("--------------------")
    print("  帳號\t密碼")
    for key in keys:
        print("  %s\t%s" %(key, data[key]))
    print("--------------------")

def edit():
    while True:
        account = input("請輸入欲修改密碼之帳號：")
        if account in data:
            password = input("請輸入新密碼：")
            data[account] = password
            with open(file_name, 'w') as file:
                file.write(str(data))
            print("帳號 %s 的密碼修改成功！" %(account))
            break
        else:
            print("輸入的帳號不存在！")

def delete():
    while True:
        account = input("請輸入欲刪除的帳號資料：")
        if account in data:
            del data[account]
            print("帳號 %s 已刪除！" %(account))
            break
        else:
            print("輸入的帳號不存在")

# main
data = {}
file_name = 'pwd.txt'
if os.path.exists(file_name):
    with open(file_name, 'r') as file:
        data = eval(file.read())
else:
    f = open(file_name,'w')
    f.write(str(data))

options = {
1:create,
2:show,
3:edit,
4:delete
}

while True:
    display()
    action = input("請輸入欲執行之動作代碼：")
    if action.isdigit():
        action_code = int(action)
        if action_code in options:
            options[action_code]()
        else:
            break
    else:
        break
