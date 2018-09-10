from chalice import Chalice, Response, CORSConfig
import os
import json

cors_config = CORSConfig(
    allow_origin='*',
    allow_headers=['Content-Type','X-Amz-Date','Authorization','X-Api-Key','X-Amz-Security-Token'],
    allow_credentials=True
)

app = Chalice(app_name='lambda-python-sample')

@app.route('/', methods=['GET'], cors=cors_config)
def rootFunction():
    Response(body={'Status': 'Ok'}, status_code=200, headers={'Content-Type': 'application/json'})
