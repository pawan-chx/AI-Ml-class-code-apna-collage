data = True
line = 1
word = "Python"

with open(r"Python Fundamentals(Part 5)\sample.txt", "r") as f:
    while data:
        data = f.readline()
        if not data:
            break

        if word in data:
            print(f"{word} found at line {line}")
            break

        line += 1




         