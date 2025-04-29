# Cloud Assignment DAY 1

## Task 1: EC2 and Storage Management. 
- Subtask 1.1: Launch a Private Linux EC2 instance. (Choose Ubuntu with t2. micro). 
- Subtask 1.2: Create an EBS volume with 10GB of storage, attach it to the created 
instance, and resize the volume to 15GB ensure the change reflects inside the instance. 
- Subtask 1.3: Deploy a sample nginx page in a private EC2 instance via init script and 
expose it via an Application Load Balancer

![alt text](image.png)

![alt text](image-14.png)

![alt text](image-2.png)

![alt text](image-16.png)


## Task 2: Serverless Architecture Setup. 
- Subtask 2.1: Create a sample Python Lambda function. 
- Subtask 2.2: Set the Lambda trigger as SQS and send a message to test the invocation. 
- Subtask 2.3: Attach the proof of lambda invocation through SQS. Attach screenshots of 
CloudWatch logs with the message from Lambda test invocation.

![alt text](image-3.png)

![alt text](image-4.png)

![alt text](image-5.png)

## Task 3: Static Website Hosting and S3 Management. 
- Subtask 3.1: Create a private S3 bucket and enable versioning to host a static website 
and upload index.html and error.html pages. Block Public access for S3 bucket.
- Subtask 3.2: Add a lifecycle rule to the bucket: Transition from Standard to Standard-IA 
in 30 days and expire objects in 200 days. Enable versioning and re-upload any 2 files to 
verify. 
- Subtask 3.3: Host the site for above S3 static website using cost effective way.

![alt text](image-6.png)

![alt text](image-7.png)

![alt text](image-8.png)


## Task 4: IAM Role attachment and Connectivity. 
- Subtask 4.1: Create a Private Instance. (Note: Choose t2. micro, Ubuntu) 
- Subtask 4.2: Create an IAM Role that can only access the S3 bucket that you have created 
in the previous question, attach the IAM role to the private instances and confirm that you 
have connectivity and push the nginx conf file to S3 via E2 machine. 

![alt text](image-17.png)

![alt text](image-12.png)

![alt text](image-13.png)

Task 5: Containerization and Content Distribution. 
- Subtask 5.1: Build a nginx Docker image, push it to Elastic Container Registry (ECR), and 
deploy the image into ECS (Elastic Container Service), exposing it via an Application Load 
Balancer. The ECS Cluster is already created in the AWS account (ecs-hu-devops). 

![alt text](image-10.png)

![alt text](image-9.png)

![alt text](image-11.png)

## assignment done

# Cloud Assignment DAY 2

```
aws ec2 create-security-group --group-name u-devops-25-rkishorzode-sg-allow-80 --description "Security group for web server allowing HTTP" --vpc-id vpc-040e583668e43adf1
```
![alt text](image-18.png)

```
aws ec2 authorize-security-group-ingress --group-id sg-0b323de7fc45b8c43 --protocol tcp --port 80 --cidr 0.0.0.0/0
```
![alt text](image-20.png)

```
aws ec2 run-instances --image-id ami-0e449927258d45bc4 --count 1 --instance-type t2.micro --key-name rkishorzode-key --security-group-ids sg-0b323de7fc45b8c43 --subnet-id subnet-041b4bd98bb3fcb39 --associate-public-ip-address --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=hu-devops-25-rkishorzode-ec2}]'

```
![alt text](image-19.png)

![alt text](image-21.png)

### ssh and install nginx
```
sudo yum update -y
sudo yum install nginx -y
sudo systemctl enable nginx
sudo systemctl start nginx
```
![alt text](image-22.png)

```
aws elbv2 create-target-group \
    --name hu-devops-25-rkishorzode-tg \
    --protocol HTTP \
    --port 80 \
    --vpc-id vpc-040e583668e43adf1 \
    --target-type instance

```
![alt text](image-27.png)

```
aws elbv2 register-targets \
    --target-group-arn arn:aws:elasticloadbalancing:us-east-1:714532077193:targetgroup/hu-devops-25-rkishorzode-tg/074fd05f612174ba \
    --targets Id=i-0a83d921699ba131f

```

![alt text](image-24.png)

![alt text](image-25.png)

```
aws ec2 create-security-group \
    --group-name hu-devops-25-rkishorzode-alb-sg \
    --description "Security group for ALB allowing HTTP" \
    --vpc-id vpc-040e583668e43adf1
```
```
aws ec2 authorize-security-group-ingress \
    --group-id sg-0d1a769c5b7f12662 \
    --protocol tcp \
    --port 80 \
    --cidr 0.0.0.0/0
```
![alt text](image-26.png)

```
aws elbv2 create-load-balancer \
    --name hu-devops-25-rkishorzode-alb \
    --subnets subnet-041b4bd98bb3fcb39 subnet-07420ce3b6966f11e \
    --security-groups sg-0d1a769c5b7f12662 \
    --scheme internet-facing \
    --type application \
    --ip-address-type ipv4
```

![alt text](image-28.png)

```
aws elbv2 create-listener \
    --load-balancer-arn arn:aws:elasticloadbalancing:us-east-1:714532077193:loadbalancer/app/hu-devops-25-rkishorzode-alb/693f2a468998ed39 \
    --protocol HTTP \
    --port 80 \
    --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-east-1:714532077193:targetgroup/hu-devops-25-rkishorzode-tg/074fd05f612174ba
```

![alt text](image-29.png)

![alt text](image-30.png)

![alt text](image-31.png)

