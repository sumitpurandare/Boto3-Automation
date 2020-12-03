import boto3

aws_mgm_con = boto3.session.Session()
s3_object = aws_mgm_con.client('s3')
paginator = s3_object.get_paginator('list_objects')
page_iterator= paginator.paginate(Bucket='dev-boto3-bucket-01')
for each in page_iterator:
    print(each)

dir(s3_object)