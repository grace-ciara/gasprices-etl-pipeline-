import http.client
import os 
import json
from dotenv import load_dotenv

load_dotenv()

def extract_gasprices(): 
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = { 
    'content-type': "application/json", 
    'authorization': f"apikey {os.getenv('GASPRICES_API_KEY')}" 
}

    conn.request("GET", "/gasPrice/stateUsaPrice?state=WA", headers=headers)

    res = conn.getresponse()
    data = res.read()

    gas_data = json.loads(data.decode("utf-8"))

    print(json.dumps(gas_data, indent=4))
    gasprices = [gas_data['result']]
    return gas_data