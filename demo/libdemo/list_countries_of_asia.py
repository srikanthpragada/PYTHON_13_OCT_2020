import requests

resp = requests.get("https://restcountries.eu/rest/v2/region/asia")
if resp.status_code != 200:
    print('Sorry! Could not get details of countries!')
    exit(0)

countries = resp.json()  # Convert JSON to dict
for country in sorted(countries, key=lambda c: c['population'], reverse=True)[:10]:
    print(f"{country['name']:50} {country['population']:10}")
