import requests

city=input("enter the name of the city\n")


url=f"https://api.weather.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r=requests.get(url)
print(r.text)














