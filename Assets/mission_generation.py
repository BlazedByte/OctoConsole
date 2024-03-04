import random
import datetime

def generate_date(start="1990-01-01", end=datetime.datetime.now().strftime("%Y-%m-%d")):
    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    result = start + (end - start) * random.random()
    return result.strftime("%d-%m-%Y")
def generate_pwd():
    s = ""
    leng = random.randint(6, 15)
    for i in range(leng):
        s += chr(random.randint(33, 126))
    return s
def generate_pin():
    return str(random.randint(100000, 999999))

def generate_tree(pwd_type:str):
    if pwd_type == "date":
        tree = {
            "private":{
                "holidays":"I went to london : {{date-r}},\nto paris : {{the-pwd}},\nto new-york : {{date-r}};\nI love travelling !",
                "passwords":{
                    "administrator":"The new password is when I went to Paris !",
                    "my-phone":"The password of my phone is : {{pin-code}}"
                }
            }
        }
    else:
        tree = {
            "private":{
                "holidays":"I went to london : {{date-r}},\nto paris : {{date-r}},\nto new-york : {{date-r}};\nI love travelling !",
                "passwords":{
                    "administrator":"KEEP IT SECRET ! The password is : {{the-pwd}}",
                    "my-phone":"The password of my phone is : {{pin-code}}"
                }
            }
        }
    return tree

PWD_TYPES = ["date","random"]

def complete_tree(tree:dict, pwd:str):
    ### TREES FLAGS ###
    ### {{the-pwd}} > The correct password
    # {{pin-code}} > 6 digits pin code
    # {{password}} > 6 to 15 characters password
    # {{date-r}} > random date in the format DDMMYYYY
    for key in tree:
        if type(tree[key]) == dict:
            complete_tree(tree[key], pwd)
        else:
            while "{{" in tree[key]:
                if "{{the-pwd}}" in tree[key]:
                    tree[key] = tree[key].replace("{{the-pwd}}", pwd)
                if "{{pin-code}}" in tree[key]:
                    tree[key] = tree[key].replace("{{pin-code}}", generate_pin())
                if "{{password}}" in tree[key]:
                    tree[key] = tree[key].replace("{{password}}", generate_pwd())
                if "{{date-r}}" in tree[key]:
                    tree[key] = tree[key].replace("{{date-r}}", generate_date())
    return tree

def generate_mission():
    pwd_type = random.choice(PWD_TYPES)
    if pwd_type == "date":
        pwd = generate_date()
        tree = generate_tree(pwd_type)
        tree = complete_tree(tree, pwd)
    elif pwd_type == "random":
        pwd = generate_pwd()
        tree = generate_tree(pwd_type)
        tree = complete_tree(tree, pwd)
    return (pwd,tree)