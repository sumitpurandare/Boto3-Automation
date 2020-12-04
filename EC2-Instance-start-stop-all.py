#Start and stop instance at once
import boto3
aws_mgm_con = boto3.session.Session()
ec2_con_client = aws_mgm_con.client('ec2')
ec2_con_res = aws_mgm_con.resource('ec2')
all_instance_ids = []
for each_instance in ec2_con_res.instances.all():
    all_instance_ids.append(each_instance.id)
#print(dir(ec2_con_res.instances))
waiter = ec2_con_client.get_waiter('instance_running')
print("Starting all instances")
ec2_con_res.instances.start()
waiter.wait(InstanceIds=all_instance_ids)
print("All your instances are p and running.Please check from Mgmt console")

