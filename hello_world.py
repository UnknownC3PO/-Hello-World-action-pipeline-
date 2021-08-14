import time
import json
import urllib3
import os
def lambda_handler(event, context):
    api_key = os.getenv("API_KEY",None)
    base_id = "app1yGHzBsgY0VVBd"
    table_name = "MainTable"
    base_url = "https://api.airtable.com/v0"
    url = f"{base_url}/{base_id}/{table_name}"
    http = urllib3.PoolManager()
    r = http.request('GET', url, 
                    fields={"api_key":api_key})
    airtable_response = json.loads(r.data.decode('utf-8'))
    try:
        z=[i["title"] for i in (sorted([i["fields"] for i in airtable_response["records"]],key=lambda i:i["ID"]))]
        return z[int(time.time())%len(z):]+z[:int(time.time())%len(z)]
    except:
        'z is empty'
