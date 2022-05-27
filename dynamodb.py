#Create Dynamo Db
import boto3

def create_marvel_table(dynamodb=None):
    
  dynamodb=boto3.resource('dynamodb',
    aws_access_key_id='******',
    aws_secret_access_key='*******',
    
# Table defination
    table = dynamodb.create_table(
        TableName='Marvel',
        KeySchema=[
            {
                'AttributeName': 'movie_title',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'year',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'movie_title',
                # AttributeType defines the data type. 'S' is string type and 'N' is number type
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'year',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            # ReadCapacityUnits set to 10 strongly consistent reads per second
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10  # WriteCapacityUnits set to 10 writes per second
        }
    ))
    
    #return table
    
#if __name__ == '__main__':
  # movie_table = create_devices_table()
#Print table status
   #print("Status:", movie_table.table_status)
  
