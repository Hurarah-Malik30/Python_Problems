import json

people_string = '''
{
    "people" : [
        {
            "name" : "John Smith",
            "phone":"555-666-777",
            "emails":["johnsmith@bogusemail.com","john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name" : "John Doe",
            "phone":"555-888-999",
            "emails":null,
            "has_license": true
        }
    ]
}
'''

# print(dir(json))
# data = json.loads(people_string) #loads-string into python load-file into python
# print(type(data))
# print(data)
# for person in data['people']:
#     print(person)

# for person in data['people']:
#     del person['phone']

# new_string = json.dumps(data,indent=2)
# print(new_string)

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'],state['abbreviation'])

with open('new_states.json','w') as f:
    json.dump(data,f) #first write from which we want to read and second is to which we want to write