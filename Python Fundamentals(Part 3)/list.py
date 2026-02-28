                    #LIST

#list is mutable sequence of values

# marks = [99, 44, 78, 89, 65, "pawan", 10.44]
# print(marks)
# print(len(marks))
# print(marks[1])
# marks[1] = 70    #list ke value ko change kar sakte hai using index
# print(marks)

               #slicing in list

# marks = [99, 44, 78, 89, 65, "pawan", 10.44]
# print(marks[2:7])
# print(marks[2:])
# print(marks[-5:-2])



                  #Methods

#1st is I.append(val)
#2nd is I.insert(insx, val)
#3rd is I.sort()
#4th is I.reverse()


# nums = [1, 2, 3, 4]

# #append matlab add karna last me
# nums.append(5)
# print(nums)

# #insert matlab kisi bhi index par naya value dalna
# nums.insert(2,6)
# print(nums)

# # short only increasing order matlab increasing order me kar deta hai
# nums.sort()
# print(nums)
# nums.sort(reverse=True)         #decreasing ye ulta kar deta hai yani reverse 
# print(nums)

# #reverse order
# nums.reverse()
# print(nums)




                     #loops in list

# nums = [1, 2, 3, 4, 10, 6]

# for val in nums:
#     print(val)



#question => find index of 10
nums = [1, 2, 3, 4, 10, 6, 10]   #10 ka index kaise nikale using loop in list

ind = 0
for val in nums:
    if val == 10:
        print(ind)
        break
    ind += 1

