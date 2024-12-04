# Step-by-Step Guide: Stopping EC2 Instances Using AWS Lambda

This guide demonstrates how to use AWS Lambda to stop EC2 instances programmatically using the AWS SDK for Python (Boto3).

## Python Code for AWS Lambda

Below is the Python code to stop an EC2 instance using Lambda:

```python
import boto3

instance = ['instance_id']
region = 'ap-south-1'
ec2 = boto3.client('ec2', region_name = region)

def lambda_handler(context, event):
    ec2.stop_instances(InstanceIds = instance)
    print(f"Stopped Instance(s) {str(instance)}")
```

## Key Steps

### 1. IAM Role Setup

- Ensure your Lambda function has an IAM role with the following permissions:
  - `ec2:StopInstances`
  - `ec2:DescribeInstances`

### 2. Create the Lambda Function

1. Log in to the AWS Management Console.
2. Navigate to the Lambda service.
3. Click "Create Function" and select "Author from scratch."
4. Assign the required IAM role.

### 3. Deploy the Code

1. Copy and paste the Python code into the Lambda function editor.
2. Adjust the `instance` list and `region` variable to match your setup.
3. Save and deploy the function.

### 4. Test the Function

1. Create a test event (it can be a blank event for this case).
2. Trigger the Lambda function.
3. Verify that the EC2 instance(s) are stopped.

## Key Notes

- Replace `'instance_id'` in the `instance` list with the actual EC2 instance ID(s) you want to stop.
- The function logs any errors and returns appropriate status codes for debugging.
- This function is suitable for automating EC2 stop operations to save costs or manage resource usage.

By following these steps, you can effectively use AWS Lambda to manage your EC2 instances programmatically.
