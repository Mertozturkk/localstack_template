import logging
import boto3
from botocore.exceptions import ClientError
import json
import os
"""
Python boto3 kullanarak yapılan işlemlerin aynı zamanda tanımlanan alias ile terminal üzerinden de yapıldığı örnekler

awsls s3api create-bucket --bucket localstack-bucket --region=eu-cental-1 --create-bucket-configuration LocationConstraint=eu-central-1

awsls s3 ls

awsls s3api list-objects --bucket localstack-bucket
"""
AWS_REGION = 'eu-central-1'
AWS_PROFILE = 'localstack_dev'
ENDPOINT_URL = 'http://localhost:4566'
# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')
boto3.setup_default_session(profile_name=AWS_PROFILE)
s3_client = boto3.client("s3", region_name=AWS_REGION,
                         endpoint_url=ENDPOINT_URL)


def create_bucket(bucket_name):
    """
    Creates a S3 bucket.
    """
    try:
        response = s3_client.create_bucket(
            Bucket=bucket_name, CreateBucketConfiguration={
                'LocationConstraint': AWS_REGION})
    except ClientError:
        logger.exception('Could not create S3 bucket locally.')
        raise
    else:
        return response


def list_buckets():
    """
    Lists all S3 buckets.
    """
    try:
        response = s3_client.list_buckets()
    except ClientError:
        logger.exception('Could not list S3 buckets locally.')
        raise
    else:
        return response


def update_file(bucket_name: str, file_path: str, object_name: str = None):
    try:
        if object_name is None:
            object_name = os.path.basename(file_path)
        response = s3_client.upload_file(file_path, bucket_name, object_name)
        return response
    except ClientError:
        logger.exception('Could not upload file to S3 bucket locally.')
        raise


def show_objects_in_bucket(bucket_name):
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        return response
    except ClientError:
        logger.exception('Could not get objects in S3 bucket locally.')
        raise


def delete_object_in_bucket(bucket_name, object_name):
    try:
        response = s3_client.delete_object(Bucket=bucket_name, Key=object_name)
        return response
    except ClientError:
        logger.exception('Could not delete object in S3 bucket locally.')
        raise


def delete_bucket(bucket_name):
    try:
        response = s3_client.delete_bucket(Bucket=bucket_name)
        return response
    except ClientError:
        logger.exception('Could not delete S3 bucket locally.')
        raise


def main():
    """
    Main invocation function.
    """
    bucket_name = "localstack-bucket"
    logger.info('Creating S3 bucket locally using LocalStack...')
    s3 = create_bucket(bucket_name)
    logger.info('S3 bucket created.')
    logger.info(json.dumps(s3, indent=4) + '\n')

    logger.info('Getting S3 bucket list locally using LocalStack...')
    bucket_list = list_buckets()
    logger.info('S3 bucket list:')
    for bucket in bucket_list['Buckets']:
        logger.info(bucket['Name'])

    logger.info('Uploading file to S3 bucket locally using LocalStack...')
    file_path = 's3textfile.txt'
    update_file(bucket_name='localstack-bucket', file_path=file_path, object_name='s3textfile.txt')
    logger.info('File uploaded to S3 bucket:')
    show_objects_in_bucket(bucket_name='localstack-bucket')

    logger.info('Deleting file from S3 bucket locally using LocalStack...')
    delete_object_in_bucket(bucket_name='localstack-bucket', object_name='s3textfile.txt')
    logger.info('File deleted from S3 bucket:')
    show_objects_in_bucket(bucket_name='localstack-bucket')

    logger.info('Deleting S3 bucket locally using LocalStack...')
    res = delete_bucket(bucket_name='localstack-bucket')
    logger.info('S3 bucket deleted.')
    logger.info(json.dumps(res, indent=4) + '\n')

    logger.info('Current S3 bucket list:')
    bucket_list = list_buckets()
    for bucket in bucket_list['Buckets']:
        logger.info(bucket['Name'])


if __name__ == '__main__':
    main()
