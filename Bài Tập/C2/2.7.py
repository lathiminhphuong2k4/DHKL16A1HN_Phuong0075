import json

json_data='{"name":"A","age":35,"company":"Đất Việt"}'

python_object = json.loads(json_data)

print("Đối tượng python là: \n",python_object)