Original_array = [2, 8, 9, 48, 8, 22, -12, 2]
New_array = set()

def add():
    for i in range(len(Original_array)):
        value = Original_array[i] + 2
        if value > 5:
            New_array.add(value)

add()

print(Original_array)
print(New_array)
