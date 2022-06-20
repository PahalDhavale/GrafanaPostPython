#!/usr/bin/python3
import json
import requests

purl = "http://<put your url here in the format IP:Port>/api/snapshots"

#the below payload should be as per the grafana documentation. Refer latest and make changes accordingly
payload={"dashboard": {"editable":"false","hideControls":"true","nav":[{"enable":"false","type":"timepicker"}],"rows": [{}],"style":"dark","tags":[],"templating":{"list":[]},"time":{},"timezone":"browser","title":"Home","version":5},"expires": 3600}

pheader ={"Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer <put in the bearer id here>"
        }

p = requests.post(purl,headers=pheader,json=payload)
convertedp=json.loads(p.text)
print(convertedp['url'])
