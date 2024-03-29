import json


def get_stored_username():
    """
    如果存储了用户名，就获取它
    """
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """
    提示用户输入用户名
    """
    username = input("what is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def decide_username(username):
    """
    判断用户名是否一致
    """
    print("Your name is " + username + " ?")
    choose = input("Please input y/n : ")
    if choose == 'y' or choose == 'Y':
        print("welcome back, " + username + "!")
    else:
        get_new_username()


def greet_user():
    """
    问候用户，并指出其名字
    """
    username = get_stored_username()
    if username:
        decide_username(username)
    else:
        username = get_new_username()
        print("we will remember you when you come back, " + username + "!")


greet_user()
