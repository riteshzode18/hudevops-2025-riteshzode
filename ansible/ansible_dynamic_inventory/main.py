#!/usr/bin/env python3

import boto3

def get_instances():
    ec2 = boto3.client('ec2', region_name='us-east-1')

    response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:role', 'Values': ['web']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    hosts = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if 'PublicIpAddress' in instance:
                hosts.append(instance['PublicIpAddress'])

    # Now write to /etc/ansible/hosts
    with open('/etc/ansible/hosts', 'w') as f:
        f.write('[web]\n')
        for ip in hosts:
            f.write(f"{ip} ansible_user=ec2-user ansible_ssh_private_key_file=/home/ritesh/my_key.pem\n")

if __name__ == '__main__':
    get_instances()
