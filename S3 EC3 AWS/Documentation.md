# Step-by-Step Guide: AWS S3 and EC2 Integration

This guide demonstrates the use of commands to connect an S3 bucket with an EC2 instance, enabling operations like listing buckets, uploading files, and downloading files.

## 🎥 Video Walkthrough

For a detailed visual explanation, watch the video:
[Watch on YouTube](https://youtu.be/your-video-id)

## Commands for AWS S3 and EC2 Integration

### 1. Install AWS CLI

```bash
snap install aws-cli --classic
```

### 2. Configure AWS CLI

```bash
aws configure
```

- Enter all default values by pressing `Enter` at each prompt.

### 3. List All Buckets

```bash
aws s3 ls
```

### 4. List Contents of a Specific Bucket

```bash
aws s3 ls s3://bucket-name
```

Replace `bucket-name` with the name of your S3 bucket.

### 5. Upload a File to S3

```bash
aws s3 cp file-in-ec2-machine s3://bucket-name
```

Replace `file-in-ec2-machine` with the path to the file on your EC2 instance, and `bucket-name` with the name of your S3 bucket.

### 6. Download a File from S3

```bash
aws s3 cp s3://bucket-name/file-in-bucket /directory-in-ec2-machine
```

Replace `file-in-bucket` with the name of the file in the S3 bucket and `/directory-in-ec2-machine` with the destination directory on your EC2 instance.

## Key Notes

- Ensure that the EC2 instance has an IAM role with appropriate permissions to access S3.
- Follow these commands in the specified order to achieve seamless integration.
