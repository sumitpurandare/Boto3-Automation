import boto3 

aws_mgmt_con_resource = boto3.session.Session()
iam_con_res =  aws_mgmt_con_resource.resource('iam')
for each in iam_con_res.users.all():
    print(each.user.name)