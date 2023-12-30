import json

python_object = {
    "name":"A",
    "age":35,
    "company":"Đất Việt"
}

json_data=json.dumps(python_object)

print(json_data)