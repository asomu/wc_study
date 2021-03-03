import json

with open('json_example.json', 'r', encoding='utf8') as file:
    content = file.read()
    jdata = json.loads(content)
    print(jdata)
    print(type(jdata))
    print()
    print(jdata['employees'])
    print()

    for data in jdata['employees']:
        print(data['firstName']+' : '+data['lastName'])
