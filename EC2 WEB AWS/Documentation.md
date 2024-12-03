# Step-by-Step Guide: Launching a Website Using EC2

This guide demonstrates how to launch a website on an EC2 instance using Apache. The following commands will help you set up the server and deploy a webpage.

## 🎥 Video Walkthrough

For a detailed visual explanation, watch the video:
[Watch on YouTube](https://youtu.be/LiJm4AkPlWc)

## Commands for Launching a Website

### 1. Install Apache Web Server

```bash
apt install apache2 -y
```

### 2. Navigate to the Web Root Directory

```bash
cd /var/www/html
```

### 3. Create a Subdirectory for the Response Page

```bash
mkdir response
cd response
```

### 4. Copy the HTML File to the Web Root Directory

```bash
cp /home/ubuntu/response.html /var/www/html
```

## Key Notes

- Ensure that the EC2 instance has the necessary security group rules to allow HTTP traffic (port 80).
- Test the setup by accessing the EC2 instance's public IP address in a web browser.
- The `response.html` file should contain the content of the webpage you wish to host.

By following these commands, you can successfully host a website on an EC2 instance using Apache.
