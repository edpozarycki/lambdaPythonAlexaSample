import boto3
from boto3.dynamodb.conditions import Key, Attr
import random


s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print bucket
    
### Let's see if we can get data into and out of a dynamodb table named "PozFamily"

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('PozFamilyFacts')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
print(table.creation_date_time)

"""
response = table.get_item(
    Key={
        'family_member': 'Tyler'
    }
)
item = response['Item']
print(item)

#item is a dictionary, with family member as the key. Let's get the value from the item returned.
fact = item['fact']
print("The fact is " + fact)

# Let's put an item into the PozFamily table.

table.put_item(
  Item={
        'family_member': 'Tyler',
        'fact': 'Tyler is a Hokie!',
    }
)
""" 

# Find all of the facts about Tyler
response = table.scan(
    FilterExpression=Attr('family_member').eq('Tyler')
)
items = response['Items']
print(items)
#
# let's extract some of the items
print("family member is " + items[0]['family_member'])
print("family fact is " + items[0]['fact'])

#
# Let's use a scan and get all of the family facts that exist.
#
response = table.scan()
items = response['Items']
print items
# Get the number of facts returned, which would be the size of the list.
print(type(items))
print(len(items))

# Select a random integer between 0 and the length of items
#
for data_item in items:
    random_integer = random.randint(0, (len(items)-1))
    print(random_integer)
    
# Now use the random number generated to get a family fact out of the list of entries
print("Family Fact is: " + items[random_integer]['fact'])

    