# Step-by-Step Guide: Connecting API Gateway to PUT Objects in an S3 Bucket

This guide demonstrates how to set up an API Gateway to allow PUT operations in an S3 bucket. This integration enables users to securely upload objects to S3 via API calls.

## 🎥 Video Walkthrough

For a detailed visual explanation, watch the video:

[Watch on YouTube](https://youtu.be/fs4duE2G0Go)

## Steps for API Gateway to S3 Integration

### 1. Create an S3 Bucket

1. Log in to your AWS Management Console.
2. Navigate to the S3 service and create a new bucket or select an existing bucket.

### 2. Create an API Gateway

1. Go to the API Gateway service in the AWS Management Console.
2. Create a new API (REST API).
3. Set up a resource and a method (e.g., PUT).

### 3. Configure Integration with S3

1. Choose S3 as the integration type.
2. Specify the bucket name and action (PUT).
3. Map the necessary headers and parameters for the request.

### 4. Deploy the API

1. Deploy the API to a stage (e.g., `dev`).
2. Note the endpoint URL provided after deployment.

### 5. Test the Integration

1. Use tools like Postman or `curl` to send a PUT request to the API Gateway endpoint.
2. Ensure the request includes the necessary headers and body to upload an object.

### Example `curl` Command

```bash
curl -X PUT \
     -H "Content-Type: application/octet-stream" \
     --data-binary @file-to-upload.txt \
     https://api-id.execute-api.region.amazonaws.com/dev/resource-path
```

Replace `api-id`, `region`, `resource-path`, and `file-to-upload.txt` with your specific values.

## Key Notes

- Ensure the S3 bucket policy allows API Gateway to perform PUT operations.
- API Gateway must have permissions through an appropriate IAM role.
- Test thoroughly in a development environment before deploying to production.

By following these steps, you can successfully connect an API Gateway to an S3 bucket for PUT operations.
