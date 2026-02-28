import json


    #JSON to python
json_str = '{"name": "Pawan", "isTeacher": null}'   #ye java yani json ka code hai

py_obj = json.loads(json_str)  # isse json ka code python ho jayega


print(type(py_obj), py_obj)



       #python to JSON
python_obj = {
    "name": "pawan chauhan",
    "isTeacher": None,
    "city": "andi"
}

jsonn_str = json.dumps(python_obj)
print(type(jsonn_str), jsonn_str)

