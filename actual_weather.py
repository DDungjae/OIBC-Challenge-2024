import requests
import pandas as pd
import json
weather_df_1 = []
weather_df_2 = []
'''for i in range(23, 32):
    date = '2024-10-{}'.format(str(i))
    actual_weather = requests.get(f'https://research-api.solarkim.com/data/cmpt-2024/actual-weather/{date}', headers={
                                'Authorization': f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJobk1UVmlkY3hjRVJZM3FWdnpkeEQyIiwiaWF0IjoxNzMwMTU2NzU3LCJleHAiOjE3MzE1OTY0MDAsInR5cGUiOiJhcGlfa2V5In0.2hcgpvv-8Q9n8RHnpgGxTaO6jeAFn8n00ARP9dLWMyY'
                            }).json()
    for j in actual_weather["actual_weather_1"]:
        weather_df_1.append(j)
    for k in actual_weather["actual_weather_2"]:
        weather_df_2.append(k)'''

for i in range(13, 14):
    date = '2024-11-{}'.format(str(i))
    actual_weather = requests.get(f'https://research-api.solarkim.com/data/cmpt-2024/actual-weather/{date}', headers={
                                'Authorization': f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJobk1UVmlkY3hjRVJZM3FWdnpkeEQyIiwiaWF0IjoxNzMwMTU2NzU3LCJleHAiOjE3MzE1OTY0MDAsInR5cGUiOiJhcGlfa2V5In0.2hcgpvv-8Q9n8RHnpgGxTaO6jeAFn8n00ARP9dLWMyY'
                            }).json()
    for j in actual_weather["actual_weather_1"]:
        weather_df_1.append(j)
    for k in actual_weather["actual_weather_2"]:
        weather_df_2.append(k)
original_df_1 = pd.read_csv('C:/Users/seojw/Documents/POSTECH/OIBC/OIBC_2024_DATA/data/기상실측데이터_1.csv')
original_df_2 = pd.read_csv("C:/Users/seojw/Documents/POSTECH/OIBC/OIBC_2024_DATA\data/기상실측데이터_2.csv")
weather_df_1 = pd.DataFrame(weather_df_1)
weather_df_2 = pd.DataFrame(weather_df_2)
weather_df_1 = weather_df_1[original_df_1.columns]
weather_df_2 = weather_df_2[original_df_2.columns]
weather_df_1.to_csv('C:/Users/seojw/Documents/POSTECH/OIBC/OIBC_2024_DATA/data/기상실측데이터_1.csv', mode='a', index=False, header=False)
weather_df_2.to_csv('C:/Users/seojw/Documents/POSTECH/OIBC/OIBC_2024_DATA/data/기상실측데이터_2.csv', mode='a', index=False, header=False)

# %%
'''import requests
import pandas as pd
import json
date = '2024-11-{}'.format("11")
actual_weather = requests.get(f'https://research-api.solarkim.com/data/cmpt-2024/actual-weather/{date}', headers={
                                'Authorization': f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJobk1UVmlkY3hjRVJZM3FWdnpkeEQyIiwiaWF0IjoxNzMwMTU2NzU3LCJleHAiOjE3MzE1OTY0MDAsInR5cGUiOiJhcGlfa2V5In0.2hcgpvv-8Q9n8RHnpgGxTaO6jeAFn8n00ARP9dLWMyY'
                            }).json()
print(actual_weather)'''
# %%
