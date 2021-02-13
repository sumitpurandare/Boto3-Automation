import boto3
import datetime
session = boto3.session.Session()
iam_con_re = session.resource(service_name = 'iam')
#get details of any IAM user

#iam_user_ob = iam_con_re.User('dummy_user')

#print((iam_user_ob.name))   
# print((iam_user_ob.arn))
# print((iam_user_ob.create_date.strftime('%d-%m-%Y')))
# print((iam_user_ob.user_name))

for iam_user_ob in iam_con_re.users.all():
    print((iam_user_ob.name))   
    print((iam_user_ob.arn))
    print((iam_user_ob.create_date.strftime('%d-%m-%Y')))
    print((iam_user_ob.user_name))
    print("----------------------------------")
