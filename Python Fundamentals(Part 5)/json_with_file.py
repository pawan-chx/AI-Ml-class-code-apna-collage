import json

with open(r"Python Fundamentals(Part 5)\data.json", "r") as f:
    py_obj = json.load(f)
    print(type(py_obj), py_obj)



data = {
    "name ": "Pawan chauhan",
    "age": 19,
    "isTeacher": True
}

with open(r"Python Fundamentals(Part 5)\data2.json", "w") as f:
    json_str = json.dump(data, f, indent=4, sort_keys=True)