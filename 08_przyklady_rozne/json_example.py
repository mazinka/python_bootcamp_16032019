import json

with open('example2.json') as fp:
    data = json.load(fp)
    print(data)

with open('../example.json') as fp:

    data = json.load(fp)
    print(data)
    print(type(data))
