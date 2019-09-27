#!/usr/bin/python3
#############################################
#  Script  to convert CSV to JSON &         #
#  TAG AWS INSTANCES using JSON DATA.       #
#  Author: Erick Soi                        #
#  version 1.0                              #
#############################################

import json, boto3, csv


## Reading Input CSV File & Convertion to JSON
csv_filename ='ConvertToJSON.CSV'

with open(csv_filename) as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

## Convert csv data into json and write it
json_file = 'json_output.json'
with open(json_file, "w") as f:
	json.dump(rows, f, sort_keys=True, indent=4, separators=(',', ': '))


## Read the JSON FILE
## Create List for Keys & Lists from the JSON File
json_test_file = 'json_output.json'
AMI_input_id_list = []	#List to hold AMI ids of the instances we want to tag
Key_list = []	#List to hold keys of tags
Value_list = []	#List to hold values of tags

with open('json_output.json', 'r') as f:
     data = json.load(f)
     for items in (data):
     	Keys = list(items.keys())
     	Key_list.append(Keys)
     	Values = list(items.values())
     	Value_list.append(Values)
 
for AMI in data:									
	AMI_input_id_list.append(AMI["ami-id"])



##Read AWS instance metedata using boto3 module
instance_list = []	#List to hold instances and their meta data
Console_AMI_id_list = [] #List to hold console AMI ids
Servers_to_tag = []	#List to hold the instances we want to tag. (lest we tag everything)

##Sample working with N.Carlifonia (us-west-1) Region
region = 'us-west-1'
ec2 = boto3.resource('ec2', region)
ec2client = boto3.client('ec2',region)				
response = ec2client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        image_id = (instance["ImageId"])
        instance_list.append(instance)
        Console_AMI_id_list.append(image_id)

## Search through all instances and fetch the AMI-ids
## Check if the AMI_IDs from the AWS are on the JSON data
## IF so create a list of servers to be Tagged based on the existence of AMIs picked from the JSON File
for server in instance_list:
	AMI = server["ImageId"]
	if AMI in AMI_input_id_list:
		Servers_to_tag.append(server)


## Tag the instances according to AMI_IDs read from the JSON Data. 
for keys, values in zip(Key_list, Value_list):
	for server in Servers_to_tag:
		if server["ImageId"] in values:
			print("Tagging: [%s] " %server["InstanceId"] + "\n")
			for key, value in zip(keys, values):
				print("Applying tag [%s] on Instance [%s]" % (value,server["InstanceId"]))
				ec2.create_tags(Resources=[server["InstanceId"]], Tags=[{'Key':key, 'Value':value}])
			print('--Successfully Tagged Instance--\n' )
