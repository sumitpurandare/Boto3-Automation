#performing all Ec2 instance operations 
import boto3

aws_mgm_con = boto3.session.Session()
ec2_dashboard_res = aws_mgm_con.resource(service_name='ec2')
ec2_dashboard_client = aws_mgm_con.client(service_name='ec2')

#print(dir(ec2_dashboard_res.instances.all()))
#print(dir(ec2_dashboard_client.start_instances))

instance_list = []
for each in ec2_dashboard_res.instances.all():
    instance_list.append(each.id)
#To Start EC2 instance
# ec2_dashboard_res.instances.start()
# waiter = ec2_dashboard_client.get_waiter('instance_running')
# waiter.wait(InstanceIds = instance_list )
# print("<<<<<<---You Instance is up and running now---->>>>>>>")


#print(instance_list)
#To Stop EC2 Instances 
ec2_dashboard_res.instances.stop()
waiter = ec2_dashboard_client.get_waiter('instance_stopped')
waiter.wait(InstanceIds = instance_list)
print("<<<<<<---You Instance has been stopped now---->>>>>>>")

