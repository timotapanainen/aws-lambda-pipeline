import json

print("loading function")

def handler(event, context):
    print(json.dumps(event))
    return "Hello World"