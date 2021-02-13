import boto3

aws_mgm_con = boto3.session.Session()
list_ec2 = aws_mgm_con.resource('ec2')
for each_instance in list_ec2.instances.all():
    print(each_instance.id,each_instance.state)