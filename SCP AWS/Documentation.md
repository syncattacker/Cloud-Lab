# 🛠️ Step-by-Step Guide: Launching 🌐 EC2, Connecting via 🔑 SSH, and Using 🚀 SCP for File Transfer

This guide provides a step-by-step explanation of launching an EC2 instance, connecting to it using SSH with a `.pem` 🔑, and transferring 📂 from a 🖥️ to the EC2 instance using the `scp` command.

## Step 1: Launching an EC2 Instance

1. **Log in to AWS Management Console**:
   - Go to [AWS Console](https://aws.amazon.com/console/).
2. **Navigate to EC2 Service**:
   - Click on the EC2 service in the console.
3. **Launch Instance**:
   - Click the "Launch Instance" button.
   - Choose an 🖼️ Amazon Machine Image (AMI).
   - Select an instance type based on your requirements.
4. **Configure Instance Details**:
   - Select the VPC and subnet.
   - Configure any additional instance details as needed.
5. **Add Storage**:
   - Allocate the required 💾.
6. **Add Tags** (optional):
   - Assign 🏷️ for easier identification.
7. **Configure Security Group**:
   - Add an inbound rule to allow 🔑 SSH (port 22).
   - Optionally, allow 🌐 HTTP/HTTPS traffic if you plan to host a 🌎 server.
8. **Key Pair Selection**:
   - Create a new 🔑 pair or use an existing one.
   - Download the `.pem` 🔑 if creating a new 🔑 pair.
9. **Launch Instance**:
   - Review your ⚙️ and launch the instance.

## Step 2: Connecting to the EC2 Instance via SSH

1. **Ensure the `.pem` 🔑 File Has Correct Permissions**:
   ```bash
   chmod 400 /path-to-ssh-key/ssh-key.pem
   ```
2. **Connect to the Instance**:
   - Use the `ssh` command to connect.
   ```bash
   ssh -i /path-to-ssh-key/ssh-key.pem ubuntu@public-ip-of-instance
   ```
   Replace the placeholders:
   - `/path-to-ssh-key/ssh-key.pem` with the path to your `.pem` 🔑.
   - `public-ip-of-instance` with your instance’s public 🌐 address.

## Step 3: Copying 📂 to the EC2 Instance Using SCP

1. **Command Syntax**:
   ```bash
   scp -i /path-to-ssh-key/ssh-key.pem /path-to-file/filename.extension ubuntu@public-ip-of-instance:/upload-directory
   ```
2. **Explanation**:
   - `scp`: Secure copy command.
   - `-i /path-to-ssh-key/ssh-key.pem`: Specifies the 🔑.
   - `/path-to-file/filename.extension`: Full path to the 📂 you want to transfer.
   - `ubuntu@public-ip-of-instance`: The 🧑‍💻 and 🌐 IP of the EC2 instance.
   - `/upload-directory`: The destination 📂 on the EC2 instance.
3. **Example**:
   - To copy a 📄 named `example.txt` from your 🖥️ to the `/home/ubuntu` 📂 on the EC2 instance:
   ```bash
   scp -i /home/user/aws-keys/mykey.pem /home/user/documents/example.txt ubuntu@192.0.2.0:/home/ubuntu
   ```
4. **Verify the 📂 Transfer**:
   - Log in to the EC2 instance and check the destination 📂 to confirm the 📂 transfer:
   ```bash
   ssh -i /path-to-ssh-key/ssh-key.pem ubuntu@public-ip-of-instance
   ls /upload-directory
   ```

## 🎥 Video Walkthrough

For a complete visual demonstration, watch the video below:

[![EC2 Setup Walkthrough](https://img.youtube.com/vi/si12uVHvtyg/1.jpg)](https://youtu.be/si12uVHvtyg)

## ✅ Conclusion

You’ve successfully launched an EC2 instance, connected to it via 🔑 SSH, and transferred 📂 using the `scp` command. This setup is essential for securely managing and interacting with your EC2 instance.
