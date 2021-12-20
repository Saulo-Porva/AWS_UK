import boto3 as boto
import sys
import json



role_to_assume_arn="arn:aws:iam::xxxxxxxxxxxx:role/AWSxxxx_xxxxxxAdminaccess_xxxxx24fexxx"
role_session_name='AssumeRoleSession1'


client = boto.client('sts', aws_access_key_id=key, aws_secret_access_key=sec_key, region_name=region_name)

assumed_role_object=client.assume_role(
    RoleArn="arn:aws:iam::xxxxxxxxxxxx:role/AWSxxxx_xxxxxxAdminaccess_xxxxx24fexxx",
    RoleSessionName="Sess1",
)

creds=assumed_role_object['Credentials']

sts_assumed_role = boto3.client('sts',
    aws_access_key_id=creds['AccessKeyId'],
    aws_secret_access_key=creds['SecretAccessKey'],
    aws_session_token=creds['SessionToken'],
)

rds_client = boto.client('rds',
                         aws_access_key_id=creds['AccessKeyId'],
                         aws_secret_access_key=creds['SecretAccessKey'],
                         aws_session_token=creds['SessionToken']
                         )