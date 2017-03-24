#!/usr/bin/python
import boto3
from ipwhois import IPWhois

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

instances=ec2_client.describe_instances()
uniq_secGroupList={}


def get_cidre_from_lookup(ip, field):
    if ip not in "0.0.0.0":
        obj = IPWhois(ip)
        res=obj.lookup()
        if field == 'range':
            return res['nets'][-1]['range']
        elif field == 'description':
            return res['nets'][-1]['description']
        elif field == 'cidr':
            return res['nets'][-1]['cidr']
        else:
            return None
    else:
        return None

def get_cidre_from_file(cidr):
    file=open('ip_list.csv', 'r')

    if cidr is not None:
        for line in file:
            if cidr in line:
                return True
    else:
        return False


def get_instances_descriptions():
    ec2_details=[]
    for i in instances['Reservations']:
        inst_id = i['Instances'][0]['InstanceId']
        inst_name = i['Instances'][0]['Tags'][0]['Value']
        sec_groups = i['Instances'][0]['SecurityGroups']
        ec2_details.append([inst_id, inst_name, sec_groups])
    return ec2_details

def print_instances(inst_list):
    for inst in inst_list:

        print "Instance ID =", inst[0], "Instance name =", inst[1]
        groups=inst[2]
        for group in groups:
            print 'SecurityGroup',group['GroupName'], group['GroupId']
            uniq_secGroupList.update({group['GroupName']:group['GroupId']})

def get_uniq_secGroupList():
    for key in uniq_secGroupList:
        print "______________________________________________"
        print "GroupName", key, 'GroupId', uniq_secGroupList[key]
        get_security_group_details(uniq_secGroupList[key])

def get_security_group_details(id):
    group=ec2_resource.SecurityGroup(id)
    for rule in group.ip_permissions:
        rule_cidr=rule['IpRanges'][0]['CidrIp']
        rule_IpProtocol = rule['IpProtocol']
        rule_FromPort = rule['FromPort']
        rule_ToPort = rule['ToPort']

        rule_ip = rule_cidr.split("/")[0]

        lookup_cidr=get_cidre_from_lookup(rule_ip, 'cidr')
        lookup_description = get_cidre_from_lookup(rule_ip, 'description')

        if get_cidre_from_file(lookup_cidr):
            status="VALID"
        else:
            status="INVALID"

        print "Rule ID", id, '\n',\
              'IpProtocol =', rule_IpProtocol,'\n',\
              'FromPort =', rule_FromPort, '\n',\
              'ToPort =', rule_ToPort, '\n',\
              'IpRanges =', rule_cidr, '\n',\
              'cidr status =', status, '\n',\
              'Ccidr_owner =',lookup_description,'\n'





instances_list=get_instances_descriptions()

print "==== List of instances ===="
print_instances(instances_list)
print "==== Uniq groups list with assigned rules and validated IP range ===="
get_uniq_secGroupList()


