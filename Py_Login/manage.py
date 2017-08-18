import os,ast

def menu():
    os.system('clear')
    print('帳號密碼管理系統：')
    print('====================')
    print('1. 輸入帳號密碼：')
    print('2. 顯示帳號密碼：')
    print('3. 修改密碼：')
    print('4. 刪除')
    print('5. 結束程式')
    print('====================')

def checkFile():
    file = "test.txt"
    if os.path.exists(file):
        return True
    else:
        print(file + ' not exists')
        return False

def readData():
    with open('test.txt','r', encoding = 'utf-8-sig') as f:
        filedata = f.read()
        if filedata != "":
            data = ast.literal_eval(filedata)
            return data
        else:
            return dict()

def disp_data():
    print('帳號 \t 密碼')
    print('============================')
    for key in data:
        print('= 帳號：{} \t 密碼：{} ='.format(key,data[key]))
    print('============================')
    input('Plz input any key return menu')

def input_data():
    while True:
        name = input('請輸入帳號： ')
        if name == '': break
        if name in data:
            print('{} 帳號已經存在 ！'.format(name))
            continue
        password = input('請輸入密碼：')
        data[name] = password
        with open('test.txt','w', encoding = 'utf-8-sig') as f:
            f.write(str(data))
        print('{} 已被儲存完畢！'.format(name))
        input('Plz input any key return menu')
        break


def edit_data():
    while True:
        name = input('請輸入要修改的帳號：')
        if name == "": break
        if not name in data:
            print('{} 帳號不存在 ！'.format(name))
            continue
        print('原來的密碼為：{}'.format(data[name]))
        password = input('請輸入新密碼：')
        data[name] = password
        with open('test.txt','w', encoding = 'utf-8-sig') as f:
            f.write(str(data))
            input('密碼更改完畢！ Plz input any key return menu')
            break

def delete_data():
    while True:
        name = input('請輸入要刪除的帳號： ')
        if name == "": break
        if not name in data:
            print('{} 帳號不存在喔！！'.format(name))
            continue
        print('確定刪除 {} 的資料？ ：'.format(name))
        ans = input("(Y/N)? : ")
        if (ans == 'Y' or ans == 'y'):
            del data[name]
            with open('test.txt','w', encoding = 'utf-8-sig') as f:
                f.write(str(data))
                input('已經刪了，來不及了！')
                break

data = dict()
data = readData()
while True:
    menu()
    try:
        chi = int(input("輸入選擇："))
        print()
        if chi == 1:
            input_data()
        elif chi == 2:
            disp_data()
        elif chi == 3:
            edit_data()
        elif chi == 4:
            delete_data()
        elif chi == 5:
            break
        else:
            print("輸入錯誤，請重新輸入！")
            input('Plz input any key return menu')
            os.system('clear')
            continue
    except:
            print("輸入錯誤，請重新輸入！")
            input('Plz input any key return menu')
            os.system('clear')
            continue



print('掰囉！下次見！')
