import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info('got event{}'.format(event))
    return {'message': 'Hello World'}
