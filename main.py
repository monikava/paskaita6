
print("\n1 Užduotis")
print("\n----read----readline----readlines----\n")

text = open('.\\files\\tekstas.txt')
read_text = text.read()
# readline_text = text.readline()
# readlines_text = text.readlines()

print("Read text: \n" + read_text)
# print(readline_text)
# print(readlines_text)

other_text = text.read()
print("\nOther text: \n" + other_text)

text.close()

print("\n----seek----\n")

text = open('.\\files\\tekstas.txt')
read_text = text.read()
print("Read text: \n" + read_text)

text.seek(0)
seek_text = text.read()
print("\nSeek text: \n" + seek_text)
text.close()

print("\n----with----\n")

with open('.\\files\\tekstas.txt') as file:
    text = file.read()
print(text)

file = open('.\\files\\tekstas.txt')
text = file.read()
print("\n" + text)

print(file.closed)
file.close()
print(file.closed)
# print(file.read())

file = open('.\\files\\tekstas.txt')
text = file.read()
close_text = file.close()
print(file.closed)

with open('.\\files\\tekstas.txt') as file:
    text2 = file.read()
print(file.closed)

with open('.\\files\\tekstas.txt') as file2:
    line = file2.readline()
    print(line)
    line = file2.readline()
    print(line)
    line = file2.readline()
    print(line)
    line = file2.readline()
    print(line)
    line = file2.readline()
    print(line)

with open('.\\files\\tekstas.txt') as file3:
    line2 = file3.readlines()
    print(line2)

# padariau ties 11

