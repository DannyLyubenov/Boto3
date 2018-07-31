import boto3

path = "data.txt"
file = open(path, "w")

ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        if 'KeyName' in instance.keys():
            ec2Dict = {
                "Name": instance["KeyName"],
                "ID": instance["InstanceId"],
                "Type": instance["InstanceType"],
                "IP Address": instance["PrivateIpAddress"],
                "State": instance["State"]["Name"],
                "Group": instance["SecurityGroups"][0]["GroupId"]
            }
        else:
            ec2Dict = {
                "Name": "No Name",
                "ID": instance["InstanceId"],
                "Type": instance["InstanceType"],
                "IP Address": instance["PrivateIpAddress"],
                "State": instance["State"]["Name"],
                "Group": instance["SecurityGroups"][0]["GroupId"]
            }
        for i, j in ec2Dict.items():
            file.write(str(i) + " - " + str(j) + "\n\n")
            print(str(i) + " - " + str(j))
        file.write("-------------" + "\n\n")
        print("\n" + "-------------" + "\n")

file.close()
