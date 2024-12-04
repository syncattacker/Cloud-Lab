import boto3
instance = ['instance_id']
region = 'ap-south-1'
ec2 = boto3.client('ec2', region_name = region)

def lambda_handler(context, event):
    ec2.stop_instances(InstanceIds = instance)
    print(f"Stopped Instance(s) {str(instance)}")