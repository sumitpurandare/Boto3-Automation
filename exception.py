import sys
try:
    import boto3
    import botocore
except ModuleNotFoundError:
    print("Boto3 module is not installed.PLease instaled it using PIP ")
    sys.exit(1)

try:
    aws_man_con = boto3.session.Session()
except botocore.exceptions.ProfileNotFound:
    print("root profile is not found plese configure in .aws directory ")
    sys.exit(2)

iam_mmg_con = aws_man_con.resource(service_name= 'iam')
iam_man_client = aws_man_con.client(service_name= 'iam')
for each_user in iam_mmg_con.users.all():
    print(each_user)

response = iam_man_client.list_users()
#print(response['Users'])
for each_user in response['Users']:
    print(each_user['UserName'])


