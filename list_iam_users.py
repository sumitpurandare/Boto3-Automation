import boto3

aws_mgm_con = boto3.session.Session()
iam_con=aws_mgm_con.client('iam')

for each_user in iam_con.list_users()['Users']:
    print(each_user['UserName'])
    