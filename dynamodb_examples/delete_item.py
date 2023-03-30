import json
import logging
import os
import boto3
from botocore.exceptions import ClientError

AWS_REGION = 'eu-central-1'
AWS_PROFILE = 'localstack_dev'
ENDPOINT_URL = 'http://localhost:4566'

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')
boto3.setup_default_session(profile_name=AWS_PROFILE)
dynamodb_resource = boto3.resource(
    "dynamodb", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)


def delete_dynamodb_table_item(table_name, name, email):
    """
    Deletes the DynamoDB table item.
    """
    try:
        table = dynamodb_resource.Table(table_name)
        response = table.delete_item(
            Key={
                'Name': name,
                'Email': email
            }
        )
    except ClientError:
        logger.exception('Could not delete the item.')
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
    logger.info('Deleteing item...')
    dynamodb = delete_dynamodb_table_item(
        table_name, name, email)
    logger.info(
        f'Details: {json.dumps(dynamodb, indent=4)}')


if __name__ == '__main__':
    main()
