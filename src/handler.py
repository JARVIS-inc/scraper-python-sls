import boto3
import os
import logging
import uuid
from urllib.parse import urlparse
from src.webdriver_screenshot import WebDriverScreenshot
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3', region_name = 'us-east-1')

def scrapeshot(event, context):
    logger.info("## INITIALIZING EXECUTION ##")
    logger.info('## ENVIRONMENT VARIABLES ##')
    for k, v in sorted(os.environ.items()):
        print(k+':', v)
    print('\n')
    # list elements in path environment variable
    [print(item) for item in os.environ['PATH'].split(';')]

    logger.info('## EVENT##')
    logger.info(event)
    
    try:
        logger.info("# VALIDATING EVENT #")
        validate_event(event)
    except Exception as e:
        return {
            "statusCode" : 400,
            "message" : str(e)
        }

    width = event['width']
    height = event['height']
    url = event['url']
    selectors = event['selectors']
    filename = event['filename']
    bucket = os.environ['SCRAPESHOTBUCKET']

    logger.info("## INITIALIZING WEBDRIVER ##")

    driver = WebDriverScreenshot()
    driver.take_screenshot(url, '/tmp/'+filename, selectors, width, height)
    driver.close()


    if "ISDOCKERENV" not in os.environ:
        logger.info("## UPLOADING TO S3 ##")
        s3.upload_file('/tmp/'+filename, bucket, filename) 

    body = {
        "url": "SUCCESS. Next step is to figure out a way to return file location from s3 bucket and giver temporary permissions to access it from alexa-hosted skill..."
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't usels the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """



def validate_event(event):
    try:
        result = urlparse(event['url'])
    except:
        raise Exception("Malformed URL parameter")
    
    if event['width']<0:
        raise Exception("Invalid format for width")
    
    if event['height']<0:
        raise Exception("Invalid format for height")
    
    if (".png" or ".jpg" or ".jpeg") not in event['filename']:
        raise Exception("Invalid filename . Filename must be atleast 1 character and either a .jpeg or .png")

    #TODO: Validate selectors at some point