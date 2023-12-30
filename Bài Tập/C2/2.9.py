import json

dictionary={"key1":"value1","key2":"value2","key3":"value3"}

json_data=json.dumps(dictionary,indent=4)
print(json_data)