            #Sets
    #collection of unique elements and element no dubicate

# s = {1, 2, 3, 4, 4, 5,}    #repeat wala ek aayega
# print(s)

# empy_set =  set()  # this empty set


           #methods in sets
 #1st => s.add(val)
 # 2nd  => s.remove(val)
 # 3rd  => s.clear()
 # 4th  => s.pop()
 # 5th  => s.union(set2)
 # 6th  => intersection(set2)          

s1 = {1, 2, 4, 4, 5,} 
s2 = {1, 2, 3, 4, 8, 11}

# s1.add(6)
# s1.remove(2)
# s.clear()
# s1.pop()   #rendom value remove hoga
print(s1.union(s2))
print(s1.intersection(s2))
