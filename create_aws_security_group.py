import boto3

def create_security_groups(access_key, secret_key, aws_region):
    client = boto3.client('ec2', region_name=aws_region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    response = client.create_security_group(
        Description='SG-1',
        GroupName='SG-1',
        VpcId='vpc-123',
    )

    security_group_id = response['GroupId']

    print(f"Security Group '{security_group_id}' created successfully.")

    cidr_ip = '180.0.0.0/32'
    rule_description = 'Frankfurt'
    client.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                'IpProtocol': '-1',
                'IpRanges': [{'CidrIp': cidr_ip, 'Description': rule_description}]
            }
        ]
    )

    print(f"Inbound rule added to allow traffic from {cidr_ip}.")


#def modify_inbound_rules():

if __name__ == "__main__":
    access_key = input("Enter your AWS access key: ")
    secret_key = input("Enter your AWS secret key: ")
    aws_region = input("Enter the AWS region: ")

    create_security_groups(access_key, secret_key, aws_region)
