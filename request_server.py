import requests
import json

url = "http://localhost:8000/predict"

# Properly formatted request data
data = {
  "features": [
    {
      "proto": "tcp",
      "service": "http",
      "state": "CON",
      "dur": 1.0,
      "spkts": 10,
      "dpkts": 12,
      "sbytes": 1000,
      "dbytes": 1500,
      "rate": 1.2,
      "sttl": 255,
      "dttl": 128,
      "sload": 0.5,
      "dload": 0.6,
      "sloss": 0,
      "dloss": 0,
      "sinpkt": 0.1,
      "dinpkt": 0.2,
      "sjit": 0.1,
      "djit": 0.1,
      "swin": 128,
      "stcpb": 5000,
      "dtcpb": 3000,
      "dwin": 64,
      "tcprtt": 0.5,
      "synack": 0.01,
      "ackdat": 0.02,
      "smean": 100,
      "dmean": 150,
      "trans_depth": 2,
      "response_body_len": 0,
      "ct_srv_src": 3,
      "ct_state_ttl": 4,
      "ct_dst_ltm": 2,
      "ct_src_dport_ltm": 1,
      "ct_dst_sport_ltm": 2,
      "ct_dst_src_ltm": 1,
      "is_ftp_login": 0,
      "ct_ftp_cmd": 0,
      "ct_flw_http_mthd": 1,
      "ct_src_ltm": 5,
      "ct_srv_dst": 1,
      "is_sm_ips_ports": 0
    }
  ]
}

headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    print("Success! Response:")
    print(json.dumps(response.json(), indent=2))
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
    print(f"Response content: {err.response.text}")
except Exception as e:
    print(f"Other error: {e}")