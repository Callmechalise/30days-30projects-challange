import requests
API_KEY="d472103da2ab74d7511e6d60"
x=input("Enter currency to be converted:\n").strip().upper()
y=input("Enter the currency to convert in:\n").strip().upper()
url=f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{x}/{y}"
response=requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"1 {x} = {data['conversion_rate']} {y}")
    crate=float(data['conversion_rate'])
    amount=float(input("Enter amount:\n"))
    print(f"Amount in {y}:{crate*amount}")

else:
    print(f"Error: {response.status_code}")
    print(response.json())
    