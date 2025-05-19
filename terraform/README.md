### terraform Assignment
## DAY 1

Q 1: Create an AWS IAM Role for S3 and EC2 Services Using Terraform. 

Objective: Define an AWS IAM role with the necessary policies to manage S3 buckets and EC2 instances. 

Tasks: 

Create an IAM role with permissions to access and manage AWS S3 and EC2 services. 

Attach policies that allow necessary actions on S3 and EC2, ensuring compliance with the principle of least privilege. 

![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)

![alt text](image-3.png)

Q 2: Deploy an EC2 Instance with Security Group Using Terraform 

Objective: Write a Terraform configuration to create an EC2 instance along with a security group that allows specific inbound and all outbound traffic. 

Tasks: 

Define a Terraform configuration to provision an EC2 instance. 

Configure a security group that allows inbound SSH, HTTP, and HTTPS traffic from your system's IP address, and permits all outbound traffic. 

![alt text](image-4.png)

![alt text](image-5.png)

![alt text](image-6.png)


Q 3: Use Terragrunt to Manage S3 Buckets Across Environments 

Objective: Deploy S3 buckets in multiple environments (two) using Terragrunt to manage variations in configuration. 

Tasks: 

Create a Terragrunt configuration to deploy an S3 bucket in two different environments (e.g., staging and production). 

Configure the S3 bucket settings to suit the needs of each environment, such as versioning and access policies. 



Q 4: Configure Azure Blob Storage and CDN 

Objective: Set up Azure Blob Storage and a CDN to host and distribute an HTML page. 

Tasks: 

Deploy Azure Blob Storage and upload an HTML page. 

Set up Azure CDN to serve the HTML page stored in Blob Storage, ensuring optimal load times globally. 

![alt text](image-7.png)

![alt text](image-8.png)

![alt text](image-9.png)

![alt text](image-10.png)

![alt text](image-11.png)

## cdn is giving domain error and i am not able to connect it

Q 5: Create Google Cloud Run and Container Registry 

Objective: Establish a Google Cloud Run service and a Container Registry to manage and deploy containerized applications. 

Tasks: 

Create a Google Container Registry to store Docker images. 

Deploy an application using Google Cloud Run that pulls the necessary image from the Google Container Registry. 

 

## DAY 2

Q 1. Objective: Create a CloudFormation template to deploy an AWS Lambda function. 

Tasks: 

Create a Lambda function that logs input data to CloudWatch. 

Ensure appropriate roles and permissions are configured for Lambda to write to CloudWatch.cc 

```
code: day-2/assignment-1
```



Q 2. Objective: Create a CloudFormation template to provision an S3 bucket with a lifecycle policy that transitions objects to a different storage class or deletes them after a certain period. This introduces students to AWS S3 and data lifecycle management. 

Tasks: 

S3 Bucket: Create an S3 bucket with a unique name (use AWS pseudo parameters or functions to generate unique names). 

Lifecycle Policy: Implement a lifecycle policy that archives objects to Glacier after 30 days and then deletes them after 365 days. 

Bucket Policy: Define IAM policies that grant read/write access to specific IAM roles. 

```
code: day-2/assignment-2
```


Q 3. Objective: Create a CloudFront distribution to serve content from an S3 bucket securely. 

Tasks: 

Set up an S3 bucket and upload sample content. 

Configure a CloudFront distribution to serve content from the S3 bucket. 

Implement Geo-restriction to restrict access to specific regions. 


```
code: day-2/assignment-3
```

Q 4. Objective: Deploy an Azure App Service and configure it with a custom domain. 

Tasks: 

Deploy an App Service plan and a web app. 

Configure DNS settings to link a custom domain to the web app. 

 
```
code: day-2/assignment-4
```


Q 5. Objective: Deploy an Azure Virtual Machine Scale Set (VMSS) configured for high availability 

Tasks: 

Design and Deploy VM Scale Set. 

Implement Autoscaling. 

Setup Load Balancing 


```
code: day-2/assignment-5
```
