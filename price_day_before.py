import requests

date = '2024-11-01'
smp_da = requests.get(f'https://research-api.solarkim.com/data/cmpt-2024/smp-da/{date}', headers={
                            'Authorization': f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJobk1UVmlkY3hjRVJZM3FWdnpkeEQyIiwiaWF0IjoxNzMwMTU2NzU3LCJleHAiOjE3MzE1OTY0MDAsInR5cGUiOiJhcGlfa2V5In0.2hcgpvv-8Q9n8RHnpgGxTaO6jeAFn8n00ARP9dLWMyY'
                        }).json()
print(smp_da) 
