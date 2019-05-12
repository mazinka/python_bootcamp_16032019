import urllib.request
import json
import requests

# with urllib.request.urlopen('http://api.nbp.pl/api/exchangerates/tables/A?format=json') as f:
#     #print(f.read())
#     data = json.loads(f.read())
#     rates = data[0]['rates']
#     for rate in rates:
#         print(rate)

r =requests.get('http://api.nbp.pl/api/exchangerates/tables/A?format=json')
data = r.json()
rates = data[0]['rates']


print('oferujemy waluty:')
for rate in rates:
    print(f'{rate["code"], {rate["mid"}}, ({rate["currency"]})')

code = input("jaka walute chcesz kupic")
amount= float(input('za ile pln chcesz jej kupic{code}'))


rate = None
for rate in rates:
     if r['code'] ==code:
        rate = float(r['mid'])

result = amount/rate
print(f'za {amount} pln kupisz {result:.2f} {code}')


# action = input('co chcesz kupić:' [w-wybierz walute}, 'i ile chcesz jej kupic:' [i-ile chcesz jej kupic]')
#
# if action == 'bat':
#     rates = input ('waluta')
#     ile = input('ile jednostek')
#     kalkulacja = rates*ile
#     print(kalkulacja)
# elif action =="ile":
#
#
#     for i, e in enumerate(employes, start=1):
#         print(f'-[{i}] {e["name"]} {e["last_name"]}, pensja: {e["salary"]}')