import json
import urllib3
def lambda_handler(event, context):
    base_id="app1yGHzBsgY0VVBd"
    table_name="MainTable"
    api_key="key4jDdoqZmxtIjxP"
    url = "https://api.airtable.com/v0/"+base_id+"/"+table_name+"?api_key="+api_key
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    airtable_response = json.loads(r.data.decode('utf-8'))
    z=[]
    for i in airtable_response["records"]:
        z.append(i["fields"]["title"])
    print(z)
    gen=[]
    for i in range(len(z)):
        gen.append(z.pop(-1))
        z.insert(0,gen[0])
        gen=[]
        print(z[0:3])
    return z
