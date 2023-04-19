import json
from sls_sdk import serverlessSdk
import logging
def handler(event, context):
    serverlessSdk.capture_error('This is an error')
    logging.error("This is another error")

    import http.client
    host = "docs.python.org"
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", "/3/", headers={"Host": host})
    response = conn.getresponse()
    print(response.status, response.reason)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
