import gzip
import json
import boto3
import base64
import zlib


def lambda_handler(event, context):
    
    
    encoded_data = event['awslogs']['data']
    decoded_data = base64.b64decode(encoded_data)
    decompressed_data = zlib.decompress(decoded_data, zlib.MAX_WBITS | 16)
    
    # The decompressed_data variable now contains the original log data in JSON format
    log_data = json.loads(decompressed_data)
    
    evnt= json.loads(log_data['logEvents'][0]['message'])
    event_name=evnt['eventName']
    eventTime=evnt["eventTime"]
    username= list(evnt['userIdentity']['arn'].split(':'))[-1]
    region= evnt['awsRegion']
    eventSource=evnt['eventSource']
    sIPaddrs=evnt['sourceIPAddress']
    instnce_id=evnt['responseElements']["instancesSet"]["items"][0]["instanceId"]

    
    

    sns_client= boto3.client('sns')
    
    response = sns_client.publish(
        TopicArn='arn:aws:sns:eu-north-1:280891701417:Project4',
        Subject='EC2 Instance Event',
        Message= f'EC2 instance: {event_name} \ninstance_id: {instnce_id} \nregion: {region} \ntime :{eventTime} \n username: {username} \n sourceIPAddress: {sIPaddrs} \n eventSource: {eventSource}'
    )

    
    
