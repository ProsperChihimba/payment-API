import json;
import requests;
import base64
#import pyodbc;


def send_sms(phone_no, message):
    URL = 'https://apisms.beem.africa/v1/send'
    api_key = ''
    secret_key = ''
    content_type = 'application/json'
    source_addr = ''
    apikey_and_apisecret = api_key + ':' + secret_key

    first_request = requests.post(url = URL,data = json.dumps({
    'source_addr': source_addr,
    'schedule_time': '',
    'encoding': '0',
    'message': message,
    'recipients': [
    {
    'recipient_id': 1,
    'dest_addr': phone_no,
    }
    ],
    }),
    
    headers = {
    'Content-Type': content_type,
    'Authorization': 'Basic ' + api_key + ':' + secret_key,
    },
    auth=(api_key,secret_key),verify=False)

    return (first_request.json())