#!/usr/bin/python3
import json
import sys

try:
    import boto3
except Exception as e:
    print(e)
    print("Please rectify above exception and then try again")
    sys.exit (1)

def get_hosts(ec2_ob, fv):
    f={"Name":"tag:Name", "Values": [fv]}
    hosts=[]

    for each_in in ec2_ob.instances.filter(Filters=[f]):
        #print(each in.private_ip_address)
        hosts.append(each_in.public_ip_address)
    return hosts

def main():
    ec2_ob=boto3.resource("ec2","ap-south-1")
    db_group=get_hosts(ec2_ob, 'webserver3')
    app_group=get_hosts(ec2_ob, 'loadbalancer3')

    all_groups={ 'webserver3': db_group, 'loadbalancer3': app_group }
    print(json.dumps(all_groups))
    return None

if __name__=="__main__":
    main()

