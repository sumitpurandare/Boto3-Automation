import boto3
from random import choice
import sys


def get_iam_user():
    aws_man_con = boto3.session.Session()
    iam_man_con = aws_man_con.client('iam',region_name='us-east-2')
    return iam_man_con

def get_random_password():    
    len_of_pass = 16
    chars = "abcdefghijklmnopqrstvuwxyz1234567890!@#$%^&*()_+><>~ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join(choice(chars) for each in range(len_of_pass))
def input_func():
    inp = input("ENTER A USERNAME OF YOUR CHOICE: ")
    return inp  

def main():    
    iam_client=get_iam_user()
    iam_user = input_func()
    Password = get_random_password()
    PolicyArn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
    try:
     iam_client.create_user(UserName=iam_user)
    except Exception as e:
        if e.response['Error']['Code']=="EntityAlreadyExists": 
            print(f"User {iam_user} already exists:") 
            sys.exit(2)
        else:
            print("please verify and try it again")
            sys.exit(3)
    iam_client.create_login_profile(UserName=iam_user,Password=Password,PasswordResetRequired=False)
    iam_client.attach_user_policy (UserName=iam_user,PolicyArn=PolicyArn)
    print(f"{iam_user} has been created please check creds.txt file for credentials")
    with open("creds.txt",'w',encoding = 'utf-8') as f: 
        
        f.write("UserName: ")
        f.write(iam_user)
        f.write("\n")
        f.write("Password: ")
        f.write(Password)

    return None


if __name__ == '__main__':
    main()

