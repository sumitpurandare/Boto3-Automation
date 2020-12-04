#performing all Ec2 instance operations 
import boto3

aws_mgm_con = boto3.session.Session()
ec2_dashboard_res = aws_mgm_con.resource(service_name='ec2')
ec2_dashboard_client = aws_mgm_con.client(service_name='ec2')

#print(dir(ec2_dashboard_res.instances.all()))
#print(dir(ec2_dashboard_client.start_instances))

# instance_list = []
# for each in ec2_dashboard_res.instances.all():
#     instance_list.append(each.id)
#To Start EC2 instance
# ec2_dashboard_res.instances.start()
# waiter = ec2_dashboard_client.get_waiter('instance_running')
# waiter.wait(InstanceIds = instance_list )
# print("<<<<<<---You Instance is up and running now---->>>>>>>")


#print(instance_list)
#To Stop EC2 Instances 
# ec2_dashboard_res.instances.stop()
# waiter = ec2_dashboard_client.get_waiter('instance_stopped')
# waiter.wait(InstanceIds = instance_list)
# print("<<<<<<---Your Instances has been stopped now---->>>>>>>")
# print(f"List of Instances id :{instance_list}" )

#resource object
print("-------------Resource-------------------")
test_server_ids = []
f1 = {"Name":"tag:Name","Values":['Testing-server']}
for each_ins in ec2_dashboard_res.instances.filter(Filters = [f1]):
    test_server_ids.append(each_ins)

#Client object
test_server = []
print("----------------Client-----------------")
for each_ins_cli  in ec2_dashboard_client.describe_instances(Filters = [f1])['Reservations']:
    for each_in in each_ins_cli['Instances']:
        test_server.append(each_in['InstanceId'])
print(test_server)
print("Starting instances with ids of ",test_server )
ec2_dashboard_client.start_instances(InstanceIds = test_server)
waiter = ec2_dashboard_client.get_waiter('instance_running')
waiter.wait(InstanceIds = test_server )
print("Test server has been started")
