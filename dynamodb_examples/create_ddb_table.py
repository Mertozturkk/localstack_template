import json
import logging
from datetime import date, datetime
import os
import boto3
from botocore.exceptions import ClientError
"""
awsls dynamodb list-tables

"""
AWS_REGION = 'eu-central-1'
AWS_PROFILE = 'localstack_dev'
ENDPOINT_URL = 'http://localhost:4566'


logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')
boto3.setup_default_session(profile_name=AWS_PROFILE)
dynamodb_client = boto3.client(
    "dynamodb", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)


def json_datetime_serializer(obj):
    """
    Helper method to serialize datetime fields
    """
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def create_dynamodb_table(table_name):
    """
    Creates a DynamoDB table.
    """
    try:
        response = dynamodb_client.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'Name',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'Email',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'Name',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'Email',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            },
            Tags=[
                {
                    'Key': 'Name',
                    'Value': 'localstack-dynamodb-table'
                }
            ])
    except ClientError:
        logger.exception('Could not create the table.')
        raise
    else:
        return response


def main():
    """
    Main invocation function.
    """
    table_name = 'localstack-dynamodb-table'
    logger.info('Creating a DynamoDB table...')
    dynamodb = create_dynamodb_table(table_name)
    logger.info(
        f'DynamoDB table created: {json.dumps(dynamodb, indent=4, default=json_datetime_serializer)}')


if __name__ == '__main__':
    main()
