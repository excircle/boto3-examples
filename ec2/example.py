import boto3

# creates a client capable of interacting with ec2
ec2 = boto3.resource('ec2')

# Creates a Python object, with all ec2 metadata included as obj attributes
instances = ec2.instances.all()

#loops through instance objects and prints attribute vaules
for i in instances:
    print(f"{i.id}: {i.tags}")