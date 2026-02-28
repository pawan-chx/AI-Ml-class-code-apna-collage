

squares = []
for i in range(6):
    squares.append(i*i)        #normal way using loop
print(squares)


sq = [i*i for i in range(6)]     # list comprehension
print(sq)


sq2 = [i*i for i in range(6) if i%2 != 0]     # list comprehension with condition
print(sq2)


nums = [-2, -3, 3, 4, -1, 7]
nums = [0 if val < 0 else val for val in nums]
print(nums)



words = ["hello", "pawan", "python", "Apna"]
words = [val.upper() for val in words]
print(words)
