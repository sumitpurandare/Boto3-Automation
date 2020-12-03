import boto3
from botocore.config import Config
import botocore
from botocore.exceptions import ClientError, BotoCoreError
import logging
import os

class AWSService:

   def getAvailabilityZones():

      try:
        ec2 = boto3.client('ec2', aws_access_key_id=os.getenv('aws_access_key_id'),aws_secret_access_key=os.getenv('aws_secret_access_key'), verify=False, api_version ='2016-11-15')
        response = ec2.describe_availability_zones()

        return Helper.jsonSuccess(results=response)

      except (ValueError, ClientError, BotoCoreError) as e:
        logging.exception(e)
        return Helper.jsonError(message=str(e))
        return Helper.jsonError(message=str(e))