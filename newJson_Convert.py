import json
py_data={'name':'Danish','''age''':None,'Active':'True'}
js_data=json.dumps(py_data)
print(js_data)
print(type(js_data))
new_py_data=json.loads(js_data)
print(new_py_data)

x='{"name": "Danish", "age": null, "Active":true}'
new_py_data=json.loads(x)
print(new_py_data)
print(type(new_py_data))