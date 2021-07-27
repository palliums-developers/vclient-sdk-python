import json
def json_print(data):
    print(json.dumps(data, sort_keys=True, indent=8))

def output(data):
    if isinstance(data, dict):
        json_print(data)
    else:
        print(data)
