import boto3

aws_mgm_con = boto3.session.Session(profile_name="Sumit")
ec2_con=aws_mgm_con.client('ec2')
for ec2_instance in ec2_con.describe_instances()['Reservations']:
    for list_ec2 in ec2_instance['Instances']:
        print(list_ec2['InstanceId'])
        print(list_ec2['KeyName'])