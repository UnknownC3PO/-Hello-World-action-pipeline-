import time
import json
import urllib3
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
#print(z)
#gen=[]
def lambda_handler(event, context):
    while time.time()!=0:
        for i in range(len(z)):
            gen=[]
            gen.append(z.pop(-1))
            z.insert(0,gen[0])
            gen=[]
            time.sleep(1)
            #print(z[0:3])
            return z
