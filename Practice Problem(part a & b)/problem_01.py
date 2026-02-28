
info = [
    ("Alice" , "Math"),
    ("Bob" , "Science"),
    ("Alice" , "Science"),
    ("Charlie" , "Math"),
    ("Bob" , "Math"),
    ("Alice" , "English"),
    ("Charlie", "English"),
]
uniq_sub = set()
engl_st = set()

infos = {}

for tap in info:
    name = tap[0]
    subject = tap[1]

    uniq_sub.add(subject)  #1st

    if(subject == "English"):
        engl_st.add(name)    #2nd 

    if(infos.get(name) == None):
        infos.update({name: set()})    #3rd
        infos[name].add(subject)         
    else:
        infos[name].add(subject)


print("unique subject are: " , uniq_sub)
print("All english students: " , engl_st)
print(infos)    