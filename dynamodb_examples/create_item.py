import json
import logging
import os
import boto3
from botocore.exceptions import ClientError

AWS_REGION = 'eu-central-1'
AWS_PROFILE = 'localstack_dev'
ENDPOINT_URL = 'http://localhost:4566'
# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')
boto3.setup_default_session(profile_name=AWS_PROFILE)
dynamodb_resource = boto3.resource(
    "dynamodb", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)


def add_dynamodb_table_item(table_name, name, email):
    """
    adds a DynamoDB table.
    """
    try:
        table = dynamodb_resource.Table(table_name)
        response = table.put_item(
            Item={
                'Name': name,
                'Email': email
            }
        )
    except ClientError:
        logger.exception('Could not add the item to table.')
        raise
    else:
        return response


def main():
    """
    Main invocation function.
    """
    table_name = 'localstack-dynamodb-table'
    name = 'Teleskop'
    email = 'example@cloud.com'
    logger.info('Adding item...')
    dynamodb = add_dynamodb_table_item(table_name, name, email)
    logger.info(
        f'DynamoDB table item created: {json.dumps(dynamodb, indent=4)}')


if __name__ == '__main__':
    main()
