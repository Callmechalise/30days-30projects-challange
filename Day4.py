import requests
from tabulate import tabulate
city_name="Lalitpur"
api_key="yourapi"
base_url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

respone=requests.get(base_url)
if respone.status_code == 200:
    print('Status ok')

    data=respone.json()
    weather=(data['weather'][0]['description'])#mist
    temperature=(data['main']['temp'])
    feelslike=(data['main']['feels_like'])
    humidity=(data['main']['humidity'])

    mweather=[[humidity,feelslike,weather,temperature]]
    head=["humidity","feels like(°C)","Weather","temperature(°C)"]
    print(tabulate(mweather,headers=head,tablefmt='grid'))
