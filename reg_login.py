import json
def register():
    user_name= input("enter the user name")
    user_password=input("enter your password")
    user_data={user_name:user_password}
    f=open("C:/Users/Dell/OneDrive/Documents/rajivpy/programs/loop/indexing/login.txt","a")
    json_data=json.dumps(user_data)
    f.write(json_data+"-")
# register()
def login():
    user_name= input("enter the your user name")
    user_password=input("enter your password")
    f=open("C:/Users/Dell/OneDrive/Documents/rajivpy/programs/loop/indexing/login.txt","r")
    user_data=f.read()
    user_list=user_data.split('-')
    user_login=False
    for user in user_list:
        if user!="":
            json_dic=json.loads(user)
            if user_name==json_dic and user_password==json_dic.get(user_name):
                user_login=True
    if user_login==True:
        print("login sucess")
    else:
        print("invalid login")
    f.close()



login()
