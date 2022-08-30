import json


def stylish_str(diff):
    result = json.dumps(diff, indent=1)
    result = result.replace(',', '')
    return result.replace('"', '')