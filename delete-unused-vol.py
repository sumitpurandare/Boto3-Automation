#Delete unused volumes using boto3 script
import boto3
aws_mgm_con = boto3.session.Session()
ec2_con_res = aws_mgm_con.resource(service_name ='ec2')

f_ebs_vol_unused = {"Name":"status"  ,"Values": ["available"]}
for each_vol in ec2_con_res.volumes.filter(Filters = [f_ebs_vol_unused]):
    if each_vol.tags:
        #print(each_vol.id,each_vol.state,each_vol.tags)
        print("Volume deletion is in progress...")
        response = each_vol.delete()
        print(response)

print("Untagged volume has been deleted")