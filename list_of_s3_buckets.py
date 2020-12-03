import boto3

aws_mgm_con = boto3.session.Session(profile_name="Sumit")
s3_con=aws_mgm_con.client('s3')
list_buckets = s3_con.list_buckets()
for each_s3_list in list_buckets['Buckets']:
    print(each_s3_list['Name'])