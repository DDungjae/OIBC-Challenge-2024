import json 
import requests

result = {
    'submit_result' : 
       [103.77886, 101.57492, 96.69897, 96.19668, 96.17962, 97.6279, 98.96126, 105.13026, 115.73792, 124.78367, 123.44606, 122.37989, 122.45244, 121.6284, 122.13465, 122.78983, 127.86057, 141.72693, 133.77023, 136.4493, 134.72266, 125.58971, 125.33312, 106.38692]}
success = requests.post('https://research-api.solarkim.com/submissions/cmpt-2024',
                    data=json.dumps(result),
                    headers={
                        'Authorization': 'API-KEY'
                    }).json()
print(success) 
