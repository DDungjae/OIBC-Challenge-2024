import requests

date = '2024-11-01'
smp_da = requests.get(f'https://research-api.solarkim.com/data/cmpt-2024/smp-da/{date}', headers={
                            'Authorization': 'API-TOKEN'
                        }).json()
print(smp_da) 
