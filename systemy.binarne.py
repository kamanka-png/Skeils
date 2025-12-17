#4.1
with open ("liczby.txt", "r") as file:
    content = file.readlines()
    x = 0
for i in content:
    if i.count("0")>i.count("1"):
        x= x+1
    else:
        x = x+0
print(x)

#4.2
with open("liczby.txt", "r") as file:
     content = file.readlines()
     y = 0
for line in content:
     number = int(line.strip())
     if number % 2 == 0:  
                y = y + 1
print(y)

#4.2b
with open("liczby.txt", "r") as file:
     content = file.readlines()
     y = 0
for line in content:
     number = int(line.strip())
     if number % 8 == 0:  
                y = y + 1
print(y)

#4.3
with open("liczby.txt", "r") as file:
    content = file.readlines()

min_number = float('inf')
max_number = float('-inf')
min_line = -1
max_line = -1

for index, line in enumerate(content):
     number = int(line.strip())
     if number < min_number:
            min_number = number
            min_line = index + 1 
     if number > max_number:
            max_number = number
            max_line = index + 1

print(f"Najmniejsza liczba jest w wierszu: {min_line}")
print(f"Największa liczba jest w wierszu: {max_line}")
