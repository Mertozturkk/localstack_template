import json
import logging
import os
import boto3
from botocore.exceptions import ClientError
from datetime import date, datetime

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


def delete_dynamodb_table(table_name):
    """
    Deletes the DynamoDB table.
    """
    try:
        response = dynamodb_client.delete_table(
            TableName=table_name
        )
    except ClientError:
        logger.exception('Could not delete the table.')
        raise
    else:
        return response


def main():
    """
    Main invocation function.
    """
    table_name = 'localstack-dynamodb-table'
    logger.info('Deleteing DynamoDB table...')
    dynamodb = delete_dynamodb_table(table_name)
    logger.info(
        f'Details: {json.dumps(dynamodb, indent=4, default=json_datetime_serializer)}')


if __name__ == '__main__':
    main()
