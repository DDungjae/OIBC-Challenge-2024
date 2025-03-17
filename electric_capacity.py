import requests
import pandas as pd
elec = []
'''for i in range(23, 32):
    date = '2024-10-{}'.format(i)
    smp_rt_rc = requests.get(f'https://research-api.solarkim.com/data/cmpt-2024/elec-supply/{date}', headers={
                                'Authorization': f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJobk1UVmlkY3hjRVJZM3FWdnpkeEQyIiwiaWF0IjoxNzMwMTU2NzU3LCJleHAiOjE3MzE1OTY0MDAsInR5cGUiOiJhcGlfa2V5In0.2hcgpvv-8Q9n8RHnpgGxTaO6jeAFn8n00ARP9dLWMyY'
                            }).json()
    for j in smp_rt_rc:
        price_list.append(j)'''
for i in range(13,14):

    date = '2024-11-{}'.format(str(i))
    elec_supply = requests.get(f'https://research-api.solarkim.com/data/cmpt-2024/elec-supply/{date}', headers={
                                'Authorization': f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJobk1UVmlkY3hjRVJZM3FWdnpkeEQyIiwiaWF0IjoxNzMwMTU2NzU3LCJleHAiOjE3MzE1OTY0MDAsInR5cGUiOiJhcGlfa2V5In0.2hcgpvv-8Q9n8RHnpgGxTaO6jeAFn8n00ARP9dLWMyY'
                            }).json()
    '''for j in smp_rt_rc:
        price_list.append(j)'''
    print(len(elec_supply))
    for i in elec_supply:
        elec.append(i)
elec = pd.DataFrame(elec)
elec.to_csv('C:/Users/seojw/Documents/POSTECH/OIBC/OIBC_2024_DATA/data/제주전력시장_현황데이터.csv', mode='a', index=False, header=False)

