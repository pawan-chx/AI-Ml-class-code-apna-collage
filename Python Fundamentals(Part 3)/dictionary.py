                  #DICTIONARY
      #key:value pairs

# info = {
#     "name": "pawan",
#     "last anme": "chauhan",
#     "subjects": ["python", "math"],
#     "age":19,
#     3.14:"PI",
# }

# print(info)
# print(info["name"])
# info["age"] = 20   #value ko change kar sakte hai 
# print(info)



           #Methods in dictionary
# 1st => d.keys()   return all keys  
# 2nd => d.values()   return all value
# 3rd => d.items()     return(key, value) pairs
# 4th  => d.get(val)    return value acc. to key
# 5th  => d.update(new_item)   return neew item to dict

info = {
    "name": "pawan",
    "last anme": "chauhan",
    "subjects": ["python", "math"],
    "age":19,
    3.14:"PI",
}

print(info["pawan"])
# dict_key =info.keys()
# print(dict_key)

# dict_val =info.values()
# print(dict_val)

# print(info.items())

# print(info.get("name"))

# info.update({
#     "city": "asthawan"
# })
# print(info)

