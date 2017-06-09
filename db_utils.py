"""
-Make function that takes a list of names in JSON format, populates DB with name/ID
 pairs. It will be a JSON array of strings, where each string is a name.
"""

from boto3 import client

def get_connection():
    credentials = open('.env','r').readlines()
    conn = boto3.client('dynamodb',
                          region_name='us-west-2',
                          aws_access_key_id=credentials[0].strip(),
                          aws_secret_access_key=credentials[1].strip())
    return conn

def populate_db():
    names = [i.strip() for i in open('sample_names.txt', 'r').readlines()]
    
