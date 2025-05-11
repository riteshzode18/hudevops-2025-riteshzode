import boto3
import argparse
import json

def get_instances_by_tag(tag_key, tag_value):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(
        Filters=[
            {'Name': f'tag:{tag_key}', 'Values': [tag_value]},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if 'PublicIpAddress' in instance:  # Ensure the instance has a public IP
                instances.append(instance['PublicIpAddress'])
    return instances

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true', help="List instances")
    parser.add_argument('--host', help="List details of a specific host")
    args = parser.parse_args()

    if args.list:
        instances = get_instances_by_tag('role', 'web')
        inventory = {
            'web': {
                'hosts': instances,
                'vars': {
                    'ansible_user': 'ec2-user',
                    'ansible_ssh_private_key_file': '/home/ritesh/private-key.pem'
                }
            }
        }
        print(json.dumps(inventory, indent=2))
    elif args.host:
        print(json.dumps({}))
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
